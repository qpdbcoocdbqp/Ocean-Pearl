import json
import random
from rich.console import Console
from src.theme import prettyderby


console = Console()
theme = prettyderby()
makrers = ["[DEBUG]", "[INFO]", "[WARNING]", "[ERROR]", "[MESSAGE]", "[CUSTOM]"]

# show theme
# for i, kv in enumerate(theme.items()):
#     console.print(json.dumps(kv))
#     if i > 3:
#         break

# Make color markers
characters = list(theme.keys())
random.shuffle(characters)

character = characters[0]
color_markers = [
    f"[{color.get("hex")}]{mark}[/{color.get("hex")}]"
    for mark, color in zip(makrers, theme.get(character))
    ]
print(f"Use character: {character}")
for mark in color_markers:
    console.print(mark, "log message")
