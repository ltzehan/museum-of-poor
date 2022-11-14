import os
import threading

from flask import Flask, render_template

import rospy
from bb_msgs.msg import Wildlife
from bb_msgs.srv import RobotxTaskStatus, RobotxTaskStatusRequest, RobotxTaskStatusResponse
from states import ScanTheCodeState, WildlifeState

# TODO
SCANTHECODE_SERVICE = "/display/update_scanthecode_state"
WILDLIFE_RADIO_TOPIC = "/dji_m210/task/wildlife"

app = Flask(__name__)

scanthecode_state = ScanTheCodeState()
wildlife_state = WildlifeState()

def update_scanthecode_state(req: RobotxTaskStatusRequest):
    if req.task_id == 5:
        d1 = req.data[0] // 100
        d2 = (req.data[0] // 10) % 10
        d3 = (req.data[0] // 1) % 10
        
    to_color = lambda x: {1: ScanTheCodeState.RED, 2: ScanTheCodeState.GREEN, 3: ScanTheCodeState.BLUE}[x]
    scanthecode_state.tower_color = [to_color(x) for x in [d1, d2, d3]]

    return RobotxTaskStatusResponse(True)

def update_wildlife_state(req: Wildlife):
    animals = [
        (WildlifeState.CROCODILE, req.crocodile.longitude), 
        (WildlifeState.PLATYPUS, req.platypus.longitude), 
        (WildlifeState.TURTLE, req.turtle.longitude)
    ]
    animals.sort(key=lambda x: x[1])

    wildlife_state.animal = [x[0] for x in animals]

@app.route("/")
def index():
    poor = os.listdir(os.path.join(app.static_folder, "assets", "poor"))
    return render_template("index.html", poor=poor)


@app.route("/wildlife")
def wildlife_board():
    return render_template("wildlife.html", wildlife_state=wildlife_state)


@app.route("/scanthecode")
def scanthecode_board():
    return render_template("scanthecode.html", scanthecode_state=scanthecode_state)


if __name__ == "__main__":
    threading.Thread(target=lambda: rospy.init_node("museum_of_poor", anonymous=True, disable_signals=True), daemon=True).run()
    
    # Update Scan the Code from service in BT 
    update_scanthecode_service = rospy.Service(SCANTHECODE_SERVICE, RobotxTaskStatus, update_scanthecode_state)
    # Wildlife is updated from UAV so just listen to the radio topic
    update_wildlife_sub = rospy.Subscriber(WILDLIFE_RADIO_TOPIC, Wildlife, update_wildlife_state)

    app.run(debug=True, host="0.0.0.0")
