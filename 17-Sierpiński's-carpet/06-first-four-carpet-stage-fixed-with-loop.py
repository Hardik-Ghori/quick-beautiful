from PIL import Image
from PIL import ImageDraw


def main():
    size = 300
    FRACTAL_DEPTH = 3
    carpets = []
    for i in range(-1, FRACTAL_DEPTH - 1):
        carpets.append(make_carpet(i + 1, size))

    save_animated_gif("Sierpiński's carpet.gif", carpets, 1200)

def save_animated_gif(filename, images, duration):
    """merges files into a single animated gif and saves it at the specified location"""
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image = images[0]
    other_images = images[1:]
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration, loop=0)

def make_pattern(draw, x, y, section_size, remaining_levels, hole_color):
    if remaining_levels <= 0:
        return
    corner = (x + section_size / 3, y + section_size / 3)
    # -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
    opposite_corner = (x + section_size * 2/3 - 1, y + section_size * 2/3 - 1)
    draw.rectangle((corner, opposite_corner), fill=hole_color)
    parts = 3
    for x_index in range(parts):
        for y_index in range(parts):
            x_anchor = x + section_size * x_index / parts
            y_anchor = y + section_size * y_index / parts
            new_size = section_size / 3
            new_levels = remaining_levels - 1
            make_pattern(draw, x_anchor, y_anchor, new_size, new_levels, hole_color)


def make_carpet(levels, size):
    PURPLE = (150, 0, 150)
    WHITE = (255, 255, 255)
    carpet_color = PURPLE
    carpet = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet)
    make_pattern(draw, 0, 0, size, levels, hole_color=WHITE)
    return carpet

main()