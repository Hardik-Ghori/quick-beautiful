from PIL import Image


def scale_position(from_to, value, max_value):
    return from_to[0] + (from_to[1]-from_to[0])*(float(value)/max_value)


def get_color(x, y, X, Y, WIDTH, HEIGHT):
    kx = scale_position(X, x, WIDTH)
    ky = scale_position(Y, y, HEIGHT)
    MAX_IT = 300
    c = complex(kx, ky)
    z = complex(0.0, 0.0)
    for i in range(MAX_IT):
        z = z * z + c
        if abs(z) >= 2.0:
            return (0, int(((i*1.0/MAX_IT)**0.5)*255), 0)
    return (0, 0, 0)


def mandebrot(WIDTH, HEIGHT, X, Y, filename):
    list_of_pixels = []
    for _ in range(WIDTH*HEIGHT):
        list_of_pixels.append((255, 0, 0))
    im = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = im.load()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            pixels[x, y] = get_color(x, y, X, Y, WIDTH, HEIGHT)

    im.save(filename)


WIDTH = 750
HEIGHT = 750
mandebrot(WIDTH, HEIGHT, (-1.6, 0.6), (-1.1, 1.1), "1.png")
mandebrot(WIDTH, HEIGHT, (-1.0, 0), (-1.1, -0.1), "2.png")
mandebrot(WIDTH, HEIGHT, (-0.7, -0.4), (-0.75, -0.45), "3.png")
mandebrot(WIDTH, HEIGHT, (-0.6, -0.5), (-0.7, -0.6), "4.png")
mandebrot(WIDTH, HEIGHT, (-0.55, -0.5), (-0.65, -0.6), "5.png")
