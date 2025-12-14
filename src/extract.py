# use pylette to get the colors from an image
import json
import os
from rich.console import Console
from Pylette import extract_colors
from Pylette.types import ExtractionMethod

theme_name = "prettyderby"
theme_path = f"./data/{theme_name}"
character_dir = "character"
root_path = os.path.join(theme_path, character_dir)
verbose = False

console = Console()
logo_info = extract_colors(image=os.path.join(theme_path, "logo.png"), palette_size=3, resize=True)

# view logo extract color
if verbose:
    for color in logo_info.colors:
        console.print(f"[{color.hex}]logo {color.freq:.2f}")

logo_marker = f"[bold {logo_info.colors[0].hex}][PrettyDerby][/bold {logo_info.colors[0].hex}]"
console.print(logo_marker, "Get character arts")


# Extract palette with rich metadata
img_path = []
for rpath, cpath, files in os.walk(root_path):
    if len(cpath) == 0:
        img_path.append(os.path.join(rpath, "3.png") if "3.png" in files else os.path.join(rpath, "2.png"))

console.print(logo_marker, f"Got {len(img_path)} characters")
console.print(logo_marker, "Start character extract")

output = {}
for image in img_path:
    name = image.split("\\")[-2]
    console.print(logo_marker, f"process {name}")
    try:
        char_colors = extract_colors(image=image, palette_size=6, mode= ExtractionMethod.KM, resize=True)
    except:
        continue

    # Access color properties with hex support
    if verbose:
        infos = ", ".join(map(lambda x: f"[{x.hex}][{name}][/{x.hex}] {x.freq.item():.2f}", char_colors.colors))
        console.print(logo_marker, infos)
    else:
        infos = f"[bold {char_colors.colors[0].hex}][{name}][/bold {char_colors.colors[0].hex}] {char_colors.colors[0].freq.item():.2f}"
        console.print(logo_marker, infos)
    output[name] = [
        {
            "rgb": list(map(int, color.rgb)),
            "hex": color.hex,
            "frequency": color.freq.item()
        }
        for color in char_colors.colors
        ]


console.print(logo_marker, f"Total charaters in theme: {len(output)}")

with open(f"./theme/{theme_name}.json", "w") as f:
    json.dump(output, f, indent=2)

console.print(logo_marker, "Done")
