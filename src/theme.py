import json
from enum import Enum


class THEME(str, Enum):
    PrettyDerby = "./theme/prettyderby.json"

def prettyderby():
    with open(THEME.PrettyDerby.value, "r") as f:
        theme = json.load(f)
    return theme
