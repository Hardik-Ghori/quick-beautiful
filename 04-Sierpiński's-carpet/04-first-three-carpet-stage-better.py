from PIL import Image
from PIL import ImageDraw


def save_animated_gif(filename, images, duration):
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image = images[0]
    other_images = images[1:]
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration, loop=0)

def make_pattern(draw, x, y, section_size, remaining_levels):
    if remaining_levels <= 0:
        return
    hole_color = (255, 255, 255)
    corner = (x + section_size / 3, y + section_size / 3)
    # -1 necessary due to https://github.com/python-pillow/Pillow/issues/3597
    opposite_corner = (x + section_size * 2/3 - 1, y + section_size * 2/3 - 1)
    draw.rectangle((corner, opposite_corner), fill=hole_color)
    parts = 3
    for x_index in range(parts):
        for y_index in range(parts):
            min_x_in_section = x + section_size * x_index / parts
            min_y_in_section = y + section_size * y_index / parts
            make_pattern(draw, min_x_in_section, min_y_in_section, section_size / 3, remaining_levels - 1)

def make_carpet(levels, size):
    carpet_color = (150, 0, 150)
    carpet = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet)
    make_pattern(draw, 0, 0, size, levels)
    return carpet


size = 300
carpet_without_hole = make_carpet(0, size)
carpet_with_first_hole = make_carpet(1, size)
third_carpet = make_carpet(2, size)

animation = [carpet_without_hole, carpet_with_first_hole, third_carpet]
save_animated_gif("Sierpiński's carpet.gif", animation, 1200)
