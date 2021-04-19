"""
File: mirror_qe.py
"""

from simpleimage import SimpleImage

def mirror_image(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    # Create new image to contain mirror reflection
    mirror = SimpleImage.blank(width * 2, height)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel((width * 2) - (x + 1), y, pixel)
    return mirror


def main():
    original = SimpleImage('images/qemonkey.jpg')
    original.show()

    mirrored = mirror_image('images/qemonkey.jpg')
    mirrored.show()


if __name__ == '__main__':
    main()
