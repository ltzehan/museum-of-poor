from typing import Dict, List, Tuple

from flask import Flask, render_template

app = Flask(__name__)


class WildlifeState:
    CROCODILE = "CROCODILE"
    PLATYPUS = "PLATYPUS"
    TURTLE = "TURTLE"
    UNKNOWN = "UNKNOWN"

    animal: List[str] = []
    box_color = {CROCODILE: "#00ff00", PLATYPUS: "#0000ff", TURTLE: "#ff0000", UNKNOWN: "#bbbbbb"}

    def __init__(self) -> None:
        # self.animal = [self.UNKNOWN for _ in range(3)]
        self.animal = [self.CROCODILE, self.PLATYPUS, self.TURTLE]

    def get_all_box_prop(self) -> List[Dict[str, str]]:
        return [self.get_box_prop(i) for i in range(3)]

    def get_box_prop(self, idx: int) -> Dict[str, str]:
        return {
            "text": self.animal[idx],
            "color": self.box_color[self.animal[idx]],
            "margin_top": "2cm" if idx == 0 or idx == 2 else "0",
        }


class ScanTheCodeState:
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    UNKNOWN = "UNKNOWN"

    buoy_color: List[str] = []
    box_color = {GREEN: "#00ff00", BLUE: "#0000ff", RED: "#ff0000", UNKNOWN: "#bbbbbb"}

    def __init__(self) -> None:
        self.buoy_color = [self.RED, self.GREEN, self.BLUE]
        # self.buoy_color = [self.UNKNOWN for _ in range(3)]

    def get_all_box_prop(self) -> List[Dict[str, str]]:
        return [self.get_box_prop(i) for i in range(3)]

    def get_box_prop(self, idx: int) -> Dict[str, str]:
        return {
            "text": self.buoy_color[idx],
            "color": self.box_color[self.buoy_color[idx]],
        }


wildlife_state = WildlifeState()
scanthecode_state = ScanTheCodeState()


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
    app.run(debug=True, host="0.0.0.0")
