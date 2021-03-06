from packaging import version
from PIL import Image


def main():
    """generates an animated gif of the initial stages of Sierpiński's carpet"""
    check_version()
    width = 300
    height = 300
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    im1 = Image.new("RGBA", (width, height), RED)
    im2 = Image.new("RGBA", (width, height), YELLOW)
    im3 = Image.new("RGBA", (width, height), WHITE)
    save_animated_gif("out.gif", [im1, im2, im3], 900)


def save_animated_gif(filename, images, duration):
    """
    Saves a file with animated GIF in location specified by filename parameter.
    Frames are specified as list of images in the images parameter.
    durations to display each frame are specified as a list, with milliseconds as the unit,
    list should have the same length as images list.
    """
    # done using https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving
    first_image, *other_images = images
    first_image.save(filename, save_all=True, append_images=other_images, duration=duration, loop=0)

def check_version():
    """checks whatever installed Pillow version can generate animated gifs. Protects against silent failures"""
    if version.parse(Image.PILLOW_VERSION) >= version.parse("3.4"):
        return
    print("Pillow in version not supporting making animated gifs")
    print("you need to upgrade library version")
    print("see release notes in")
    print("https://pillow.readthedocs.io/en/latest/releasenotes/3.4.0.html#append-images-to-gif")
    raise RuntimeError("upgrade pillow library, to at least 3.4")


main()
