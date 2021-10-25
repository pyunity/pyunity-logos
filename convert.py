import cairosvg
import os

for file in os.listdir("svg/logos/"):
    with open(os.path.join("svg/logos/", file)) as f:
        svg = f.read()
    
    path = os.path.join("png/convert", file)[:-3] + "png"
    cairosvg.svg2png(bytestring=svg, write_to=path)
