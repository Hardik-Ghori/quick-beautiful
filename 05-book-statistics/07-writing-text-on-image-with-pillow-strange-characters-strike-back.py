from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

width = 200
height = 200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
im = Image.new("RGB", (width, height), WHITE)
font = ImageFont.truetype("unifont-12.0.01.ttf", 14)

ImageDraw.Draw(
    im
).text(
    (10, 10),
    'zażółć gęślą jaźń!',
    BLACK,
    font=font
)

im.show()
