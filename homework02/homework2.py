from byuimage import Image


def flipped(filename):
    """takes an image and flips it vertically"""
    img = Image(filename)
    flipped_img = Image.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            o_pixel = img.get_pixel(x, y)
            n_pixel = flipped_img.get_pixel(x, (img.height-1-y))
            n_pixel.red = o_pixel.red
            n_pixel.green = o_pixel.green
            n_pixel.blue = o_pixel.blue
    return flipped_img


def make_borders(filename, thickness, red, green, blue):
    """takes an image and adds a border with custom thickness and color"""
    img = Image(filename)
    border_img = Image.blank(img.width + 2*thickness, img.height + 2*thickness)
    for y in range(border_img.height):
        for x in range(border_img.width):
            if (0 <= x <= thickness or border_img.width >= x >= (border_img.width - thickness) or
                    0 <= y <= thickness or border_img.height >= y >= (border_img.height - thickness)):
                pixel = border_img.get_pixel(x, y)
                pixel.red = red
                pixel.green = green
                pixel.blue = blue
    for y in range(img.height):
        for x in range(img.width):
            o_pixel = img.get_pixel(x, y)
            n_pixel = border_img.get_pixel(x+thickness, y+thickness)
            n_pixel.red = o_pixel.red
            n_pixel.green = o_pixel.green
            n_pixel.blue = o_pixel.blue
    return border_img


if __name__ == "__main__":
    # flipped('test_files/landscape.png').show()  # pytest test_homework2.py::test_flipped_with_landscape
    make_borders('test_files/landscape.png', 20, 150, 100, 90).show()
    #               pytest test_homework2.py::test_make_borders_landscape
    # pytest test_homework2.py
