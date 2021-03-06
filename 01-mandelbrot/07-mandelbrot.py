from PIL import Image


def get_color(x, y):
    kx = x/40.0 - 3.0
    ky = y/40.0 - 3.0
    max_it = 256
    c = complex(kx, ky)
    z = complex(0.0, 0.0)
    for i in range(max_it):
        z = z * z + c
        if abs(z) >= 2.0:
            return (255, 255, 255)
    return (0, 0, 0)


width = 500
height = 500
# https://pillow.readthedocs.io/en/latest/reference/Image.html
im = Image.new("RGB", (width, height), (255, 0, 0))
pixels = im.load()

for x in range(width):
    for y in range(height):
        pixels[x, y] = get_color(x, y)

im.save("generated.png")
im.show()
