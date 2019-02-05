from PIL import Image, ImageDraw


WIDTH = 2000
HEIGHT = 400
FIGURE_HEIGHT = 80
DWARF_CLOTHES = (240, 30, 20)
GRAY_BEARD = (240, 240, 240)
FACE_COLOR = (255, 182, 193)
GRASS = (20, 230, 20)
BACKGROUND = (110, 200, 110)
HOUSE_WALL = (230, 150, 100)
HOUSE_DOOR = (200, 120, 90)
HOUSE_ROOF = (240, 60, 60)

def hat(draw, x0, x1, head_center, r):
    head_x, head_y = head_center
    left_bottom = (x0 - 15, head_y)
    right_bottom = (x1 + 15, head_y)
    top = (head_x, head_y - 2*r)
    draw.polygon((left_bottom, right_bottom, top), fill=DWARF_CLOTHES)


def beard(draw, x0, x1, head_center, r):
    head_x, head_y = head_center
    left_top = (x0, head_y + 10)
    right_top = (x1, head_y + 10)
    bottom = (head_x, head_y + 2*r)
    draw.polygon((left_top, right_top, bottom), fill=GRAY_BEARD)


def face(draw, head_center, r):
    head_x, head_y = head_center
    circle_bounding_box = ((head_x-r, head_y-r), (head_x+r, head_y+r))
    draw.ellipse(circle_bounding_box, fill=FACE_COLOR)


def dwarf(draw, x0, y0, figure_height):
    figure_width = figure_height//2.5
    x1 = x0 + figure_width
    y1 = y0 - figure_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=DWARF_CLOTHES)
    head_x = (x0 + x1)//2
    head_y = y1
    r = figure_width // 1.5
    head_center = head_x, head_y
    face(draw, head_center, r)
    hat(draw, x0, x1, head_center, r)
    beard(draw, x0, x1, head_center, r)


def grass(draw, width, height, grass_height):
    x0 = 0
    y0 = height - 1
    x1 = width - 1
    y1 = height - grass_height
    draw.rectangle(((x0, y0), (x1, y1)), fill=GRASS)


def house_wall(draw, lower_left_anchor, wall_size):
    left_x, left_y = lower_left_anchor
    wall_width, wall_height = wall_size
    right_upper_corner = (left_x + wall_width, left_y - wall_height)
    coordinates = (lower_left_anchor, right_upper_corner)
    draw.rectangle(coordinates, fill=HOUSE_WALL)


def house_door(draw, lower_left_house_anchor, door_size):
    left_house_wall_x, house_base_y = lower_left_house_anchor
    door_width, door_height = door_size
    gap_between_door_and_wall = door_width // 2
    left_side_door_x = left_house_wall_x + gap_between_door_and_wall
    right_side_door_x = left_side_door_x + door_width
    lower_left = (left_side_door_x, house_base_y)
    upper_right = (right_side_door_x, house_base_y - door_height)
    draw.rectangle((lower_left, upper_right), fill=HOUSE_DOOR)


def house_roof(draw, lower_left_roof_anchor, roof_size):
    left_roof_anchor_x, left_roof_anchor_y = lower_left_roof_anchor
    roof_width, roof_height = roof_size
    lower_left = (left_roof_anchor_x, left_roof_anchor_y)
    lower_right = (left_roof_anchor_x + roof_width, left_roof_anchor_y)
    roof_top = (left_roof_anchor_x + roof_width//2, left_roof_anchor_y - roof_height)
    draw.polygon((lower_left, lower_right, roof_top), fill=HOUSE_ROOF)


def house(draw, lower_left_house_anchor, house_size):
    house_width, house_height = house_size
    wall_height = house_height * 2 // 3
    left_house_wall_x, house_base_y = lower_left_house_anchor

    wall_size = (house_width, wall_height)
    house_wall(draw, lower_left_house_anchor, wall_size)

    door_height = int(wall_height * 0.8)
    door_width = int(door_height * 0.4)
    door_size = (door_width, door_height)
    house_door(draw, lower_left_house_anchor, door_size)

    roof_overhang_size = house_width // 7
    lower_left_roof_anchor = (left_house_wall_x - roof_overhang_size, house_base_y - wall_height)
    roof_size = (house_width  + 2 * roof_overhang_size, house_height - wall_height)
    house_roof(draw, lower_left_roof_anchor, roof_size)


def landscape(width, height, figure_height):
    im = Image.new("RGB", (width, height), BACKGROUND)

    # https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
    draw = ImageDraw.Draw(im)
    grass_height = height // 3
    grass(draw, width, height, grass_height)

    house_width = min(300, width // 3)
    left_house_wall_x = width - house_width * 2
    house_base_y = height - grass_height // 2
    lower_left_house_anchor = (left_house_wall_x, house_base_y)
    house_height = min(figure_height * 3, int(house_base_y * 0.8))
    house_size = (house_width, house_height)
    house(draw, lower_left_house_anchor, house_size)

    x0 = 20
    y0 = height - grass_height // 2
    dwarf(draw, x0, y0, figure_height)
    dwarf(draw, x0 + 80, y0, figure_height)
    dwarf(draw, x0 + 190, y0, figure_height)
    dwarf(draw, x0 + 260, y0, figure_height)

    im.save("dwarves.png")
    im.show()


landscape(WIDTH, HEIGHT, FIGURE_HEIGHT)
