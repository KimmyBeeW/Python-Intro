from byuimage import Image


def iron_puzzle(filename):
    """ load the image, solve the puzzle by modifying the image, return the modified image"""
    img_obj = Image(filename)
    for pixel in img_obj:
        pixel.blue = pixel.blue * 10
        pixel.red = 0
        pixel.green = 0
    return img_obj


def west_puzzle(filename):
    """The hidden image is encoded using only the blue values that are less than 16 (that is, 0 through 15). If a blue
    value is less than 16, multiply it by 16 to scale it up to its proper value. Alternately if a blue value for any
    pixel is 16 or more, it is random garbage and should be ignored (interpreted as 0). The west_puzzle function should
    return the recovered image."""
    img_obj = Image(filename)
    for y in range(img_obj.height):
        for x in range(img_obj.width):
            pixel = img_obj.get_pixel(x, y)
            pixel.red = 0
            pixel.green = 0
            if pixel.blue < 16:
                pixel.blue = pixel.blue * 16
            else:
                pixel.blue = 0
    return img_obj


def darken(filename, percent):
    """The filename parameter contains the image's filename to darken, and the percent parameter tells you how much to
    darken the image by. percent must and will be a number between 0 and 1. The closer percent is to 1, the darker the
    image should be. darken should return the modified image."""
    img_obj = Image(filename)
    for y in range(img_obj.height):
        for x in range(img_obj.width):
            pixel = img_obj.get_pixel(x, y)
            pixel.red = pixel.red * (1-percent)
            pixel.green = pixel.green * (1-percent)
            pixel.blue = pixel.blue * (1-percent)
    return img_obj


def grayscale(filename):
    """returns a monochrome image (an image only in black, gray, and white).
    To make an image gray, we will use this algorithm:
        Loop through all of the pixels.
        For each pixel, calculate the average color:
            average = (pixel.red + pixel.green + pixel.blue) / 3
    Set the pixel's red, green, and blue values equal to the average."""
    img_obj = Image(filename)
    for y in range(img_obj.height):
        for x in range(img_obj.width):
            pixel = img_obj.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.red = pixel.blue = pixel.green = average
    return img_obj


def sepia(filename):
    """returns modified image that uses a sepia filter"""
    img_obj = Image(filename)
    for y in range(img_obj.height):
        for x in range(img_obj.width):
            pixel = img_obj.get_pixel(x, y)
            true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
            true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
            true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
            pixel.red = true_red
            pixel.green = true_green
            pixel.blue = true_blue
            if pixel.red > 255:
                pixel.red = 255
            if pixel.green > 255:
                pixel.green = 255
            if pixel.blue > 255:
                pixel.blue = 255
    return img_obj


def create_left_border(filename, weight):
    """adds a blue border to the left of the image given the weight"""
    img_obj = Image(filename)
    width = img_obj.width + weight
    height = img_obj.height
    new_image = Image.blank(width, height)
    for y in range(height):
        for x in range(0, weight):
            n_pixel = new_image.get_pixel(x, y)
            n_pixel.red = 0
            n_pixel.green = 0
            n_pixel.blue = 255
    for y in range(height):
        for x in range(img_obj.width):
            o_pixel = img_obj.get_pixel(x, y)
            n_pixel = new_image.get_pixel(x + weight, y)
            n_pixel.red = o_pixel.red
            n_pixel.green = o_pixel.green
            n_pixel.blue = o_pixel.blue
    return new_image


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    """Create a new blank image with the same dimensions as the image given in filename,
    but the width is an extra 50 pixels and the height is an extra 25 pixels.
    With the following priority:
        Make the pixel green if it is on a even row
        Make the pixel blue if it on a odd column (or slot)
        Otherwise, make the pixel red
        Return the newly edited image"""
    img_obj = Image(filename)
    width = img_obj.width + 50
    height = img_obj.height + 25
    new_image = Image.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel = new_image.get_pixel(x, y)
            if y % 2 == 0:
                pixel.green = 255
                pixel.red = pixel.blue = 0
            elif x % 2 == 1:
                pixel.blue = 255
                pixel.red = pixel.green = 0
            else:
                pixel.red = 255
                pixel.blue = pixel.green = 0
    return new_image



def copper_puzzle(filename):
    """The hidden image is in the blue and green values; however, all the blue and green values have all been divided
    by 20, so the values are very small. The red values are all just random numbers, noise added on top to obscure
    things. Undo these distortions to reveal the true image."""
    img_obj = Image(filename)
    for pixel in img_obj:
        pixel.blue = pixel.blue * 20
        pixel.red = 0
        pixel.green = pixel.green * 20
    return img_obj


def demo():
    """makes the image all blue"""
    cougar_image = Image("test_files/cougar.png")
    #                      ^ path to `cougar.png` file
    for pixel in cougar_image:
        pixel.red = 0
        pixel.green = 0

    cougar_image.show()


def demo2():
    cougar_image = Image("test_files/cougar.png")
    for y in range(cougar_image.height):
        for x in range(cougar_image.width):
            pixel = cougar_image.get_pixel(x, y)
    cougar_image.show()


def demo3():
    cougar_image = Image("test_files/cougar.png")
    for x in range(cougar_image.width):
        for y in range(cougar_image.height):
            pixel = cougar_image.get_pixel(x, y)
    cougar_image.show()


def blank_image():
    image = Image.blank(100, 50)  # 100 pixels wide, 50 pixels high
    image.show()


if __name__ == "__main__":
    # iron_puzzle("test_files/iron.png").show()    # pytest test_lab05.py::test_iron_puzzle
    # west_puzzle("test_files/west.png").show()    # pytest test_lab05.py::test_west_puzzle
    # darken("test_files/cougar.png", 0.3).show()  # pytest test_lab05.py::test_darken
    # grayscale("test_files/cougar.png").show()    # pytest test_lab05.py::test_grayscale
    # sepia("test_files/cougar.png").show()        # pytest test_lab05.py::test_sepia
    # create_left_border("test_files/cougar.png", 25).show()
                                                   # pytest test_lab05.py::test_create_left_border
    # create_stripes("test_files/cougar.png").show()
    # copper_puzzle("test_files/copper.png").show()
    print('done')