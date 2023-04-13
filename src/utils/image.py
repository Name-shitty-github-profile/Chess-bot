from wand.color import Color
from wand.image import Image

def svg_png(svf: str, file: str):
  with Image(filename=svf, background=Color("transparent"), resolution=144) as img:
    img.format = 'png'
    img.save(filename=file)
