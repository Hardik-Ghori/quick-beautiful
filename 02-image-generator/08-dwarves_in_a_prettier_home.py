from PIL import Image, ImageDraw


def hat(draw, x0, x1, head_x, head_y, r):
    left_bottom = (x0 - 15, head_y)
    right_bottom = (x1 + 15, head_y)
    top = (head_x, head_y - 2*r)
    draw.polygon((left_bottom, right_bottom, top), fill=(240, 30, 20))


def beard(draw, x0, x1, head_x, head_y, r):
    left_top = (x0, head_y + 10)
    right_top = (x1, head_y + 10)
    bottom = (head_x, head_y + 2*r)
    draw.polygon((left_top, right_top, bottom), fill=(240, 240, 240))


def face(draw, head_x, head_y, r):
    circle_bounding_box = ((head_x-r, head_y-r), (head_x+r, head_y+r))
    draw.ellipse(circle_bounding_box, fill=(255, 182, 193))


def dwarf(draw, x0, y0, figure_height):
    figure_width = figure_height / 2.5
    x1 = x0 + figure_width
    y1 = y0 - figure_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=(240, 30, 20))
    head_x = (x0 + x1)/2
    head_y = y1
    r = figure_width / 1.5
    face(draw, head_x, head_y, r)
    hat(draw, x0, x1, head_x, head_y, r)
    beard(draw, x0, x1, head_x, head_y, r)


def grass(draw, width, height, grass_height):
    x0 = 0
    y0 = height - 1
    x1 = width - 1
    y1 = height - grass_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=(20, 230, 20))


def house_wall(draw, lower_left_house_anchor, wall_size):
    left_house_wall_x, left_house_wall_y = lower_left_house_anchor
    wall_width, wall_height = wall_size
    right_upper_corner = (left_house_wall_x + wall_width, left_house_wall_y - wall_height)
    coordinates = (lower_left_house_anchor, right_upper_corner)
    draw.rectangle(coordinates, fill=(230, 150, 100))


def house_door(draw, lower_left_house_anchor, door_size):
    left_house_wall_x, house_base_y = lower_left_house_anchor
    door_width, door_height = door_size
    lower_left = (left_house_wall_x + door_width / 2, house_base_y)
    upper_right = (left_house_wall_x + door_width  * 1.5, house_base_y - door_height)
    draw.rectangle((lower_left, upper_right), fill=(200, 120, 90))


def house_roof(draw, lower_left_roof_anchor, roof_size):
    left_roof_anchor_x, left_roof_anchor_y = lower_left_roof_anchor
    roof_width, roof_height = roof_size
    lower_left = (left_roof_anchor_x, left_roof_anchor_y)
    lower_right = (left_roof_anchor_x + roof_width, left_roof_anchor_y)
    roof_top = (left_roof_anchor_x + roof_width/2, left_roof_anchor_y - roof_height)
    draw.polygon((lower_left, lower_right, roof_top), fill=(240, 60, 60))


def house(draw, lower_left_house_anchor, house_size):
    house_width, house_height = house_size
    wall_height = house_height * 2/3
    left_house_wall_x, house_base_y = lower_left_house_anchor

    wall_size = (house_width, wall_height)
    house_wall(draw, lower_left_house_anchor, wall_size)

    door_height = wall_height * 0.8
    door_width = door_height * 0.4
    door_size = (door_width, door_height)
    house_door(draw, lower_left_house_anchor, door_size)

    roof_overhang_size = house_width * 0.15
    lower_left_roof_anchor = (left_house_wall_x - roof_overhang_size, house_base_y - wall_height)
    roof_size = (house_width  + 2 * roof_overhang_size, house_height - wall_height)
    house_roof(draw, lower_left_roof_anchor, roof_size)


def landscape():
    width = 2000
    height = 400
    im = Image.new("RGB", (width, height), (110, 200, 110))

    # https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
    draw = ImageDraw.Draw(im)
    grass_height = int(height / 3)
    figure_height = 80
    grass(draw, width, height, grass_height)

    house_width = min(300, width / 3)
    left_house_wall_x = width - house_width * 2
    house_base_y = height - grass_height / 2
    lower_left_house_anchor = (left_house_wall_x, house_base_y)
    house_height = min(figure_height * 3, house_base_y * 0.8)
    house_size = (house_width, house_height)
    house(draw, lower_left_house_anchor, house_size)

    x0 = 20
    y0 = height - int(grass_height / 2)
    dwarf(draw, x0, y0, figure_height)
    dwarf(draw, x0 + 80, y0, figure_height)
    dwarf(draw, x0 + 190, y0, figure_height)
    dwarf(draw, x0 + 260, y0, figure_height)

    im.save("dwarves.png")
    im.show()


landscape()
