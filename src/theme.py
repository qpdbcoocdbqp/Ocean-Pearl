import os
import json
from enum import Enum
from pathlib import Path


try:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    BASE_DIR = Path.cwd()


class THEME(str, Enum):
    PrettyDerby = os.path.join(BASE_DIR, "theme", "prettyderby.json")

def prettyderby():
    with open(THEME.PrettyDerby.value, "r") as f:
        theme = json.load(f)
    return theme
