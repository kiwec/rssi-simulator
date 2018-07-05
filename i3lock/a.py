from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
from subprocess import check_output
from pathlib import Path
from shutil import copyfile

home = str(Path.home())
basedir = home + "/.config/i3/rssi-simulator/"

copyfile(basedir + "i3lock/doge.png", basedir + "i3lock/doge2.png")
img = Image.open(basedir + "i3lock/doge2.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 40)

out = check_output([basedir + "charger.sh"])
print(out.decode("utf-8"))

draw.text((980,630), out.decode("utf-8"), (255,255,255), font=font)
img.save(basedir + "i3lock/doge2.png")

