from PIL import Image
from PIL import ImageDraw

def save_animated_gif(filename, images, duration):
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image = images[0]
    other_images = images[1:]
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration)

def make_pattern(draw, x, y, section_size, remaining_levels):
    if remaining_levels <= 0:
        return
    hole_color = (5, 205, 65)
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
    carpet_color = (5, 60, 20)
    carpet = Image.new("RGBA", (size, size), carpet_color)
    draw = ImageDraw.Draw(carpet)
    make_pattern(draw, 0, 0, size, levels)
    return carpet

levels = 7
size = 3**levels
carpets = []
first_carpet = make_carpet(0, size)
durations = [400]
for i in range(levels - 1):
    carpets.append(make_carpet(i + 1, size))
    durations.append(1200)
durations[-1] *= 4

save_animated_gif.save("Sierpiński's carpet.gif", carpets, durations)
