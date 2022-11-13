import threading

from flask import Flask, render_template

import rospy
from states import ScanTheCodeState, WildlifeState

app = Flask(__name__)

scanthecode_state = ScanTheCodeState()
wildlife_state = WildlifeState()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/wildlife")
def wildlife_board():
    return render_template("wildlife.html", wildlife_state=wildlife_state)


@app.route("/scanthecode")
def scanthecode_board():
    return render_template("scanthecode.html", scanthecode_state=scanthecode_state)


if __name__ == "__main__":
    threading.Thread(target=lambda: rospy.init_node("museum_of_poor", disable_signals=True), daemon=True).run()
    rospy.Subscriber("/asv/i_dont_know_you_get_to_name_it", RobotxTaskStatus)

    app.run(debug=True, host="0.0.0.0")
