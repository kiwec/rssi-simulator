from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
from subprocess import check_output

os.system("cp /home/lexsek/Downloads/doge.png /home/lexsek/Downloads/doge2.png")
img = Image.open("/home/lexsek/Downloads/doge2.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/home/lexsek/P2A/DEV/P2M_Test/archives/46/MobSF/uploads/0a9d7da32cf6d7db5b6407321b673d3e/assets/fonts/arial.ttf",50)
out = check_output(["/home/lexsek/TOOLS/rssi-simulator/charger.sh"])
print(out.decode("utf-8"))
draw.text((980,630), out.decode("utf-8"), (255,255,255), font=font)
img.save("/home/lexsek/Downloads/doge2.png")
