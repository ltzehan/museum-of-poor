from typing import Dict, List, Tuple

class WildlifeState:
    CROCODILE = "CROCODILE"
    PLATYPUS = "PLATYPUS"
    TURTLE = "TURTLE"
    UNKNOWN = "UNKNOWN"

    animal: List[str] = []
    box_color = {CROCODILE: "#00ff00", PLATYPUS: "#0000ff", TURTLE: "#ff0000", UNKNOWN: "#bbbbbb"}

    def __init__(self) -> None:
        self.animal = [self.UNKNOWN for _ in range(3)]
        # self.animal = [self.CROCODILE, self.PLATYPUS, self.TURTLE]

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

    tower_color: List[str] = []
    box_color = {GREEN: "#00ff00", BLUE: "#0000ff", RED: "#ff0000", UNKNOWN: "#bbbbbb"}

    def __init__(self) -> None:
        self.tower_color = [self.UNKNOWN for _ in range(3)]
        # self.tower_color = [self.RED, self.GREEN, self.BLUE]

    def get_all_box_prop(self) -> List[Dict[str, str]]:
        return [self.get_box_prop(i) for i in range(3)]

    def get_box_prop(self, idx: int) -> Dict[str, str]:
        return {
            "text": self.tower_color[idx],
            "color": self.box_color[self.tower_color[idx]],
        }
