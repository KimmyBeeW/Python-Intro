import sys
from byuimage import Image


def validate_commands(args):
    """takes a list as input and return True or False depending on if the list contains a valid set of
    commands and arguments. The list passed to this function should have the operation as the first
    element and the arguments as the rest of the elements in the list."""
    if ((args[0] == "-d" and len(args) == 2) or (args[0] == "-k" and len(args) == 4 and is_float(args[3]))
        or (args[0] == "-s" or args[0] == "-g" or args[0] == "-f" or args[0] == "-m" and len(args) == 3))\
        or (args[0] == "-b" or args[0] == "-c" and len(args) == 7) or (args[0] == "-y" and len(args) == 6)\
            or args[0] == "-h":
        return True
    else:
        return False


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def darken(img, percent):
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            pixel.red = pixel.red * (1 - percent)
            pixel.green = pixel.green * (1 - percent)
            pixel.blue = pixel.blue * (1 - percent)
    return img


def sepia(img):
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
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
    return img


def grayscale(img):
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.red = pixel.blue = pixel.green = average
    return img


def make_borders(img, thickness, red, green, blue):
    """takes an image and adds a border with custom thickness and color"""
    border_img = Image.blank(img.width + 2*thickness, img.height + 2*thickness)
    for y in range(border_img.height):
        for x in range(border_img.width):
            if (0 <= x <= thickness or border_img.width >= x >= (border_img.width - thickness) or
                    0 <= y <= thickness or border_img.height >= y >= (border_img.height - thickness)):
                pixel = border_img.get_pixel(x, y)
                pixel.red = red
                pixel.green = green
                pixel.blue = blue
    border_img = framed(border_img, img, thickness, thickness)
    return border_img


def flipped(img):
    """takes an image and flips it vertically"""
    flipped_img = Image.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            o_pixel = img.get_pixel(x, y)
            n_pixel = flipped_img.get_pixel(x, (img.height-1-y))
            n_pixel.red = o_pixel.red
            n_pixel.green = o_pixel.green
            n_pixel.blue = o_pixel.blue
    return flipped_img


def mirror(img):
    mirrored_img = Image.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            o_pixel = img.get_pixel(x, y)
            n_pixel = mirrored_img.get_pixel((img.width - 1 - x), y)
            n_pixel.red = o_pixel.red
            n_pixel.green = o_pixel.green
            n_pixel.blue = o_pixel.blue
    return mirrored_img


def framed(new_img, img, x_change, y_change):
    for y in range(img.height):
        for x in range(img.width):
            o_pixel = img.get_pixel(x, y)
            pixel = new_img.get_pixel(x + x_change, y + y_change)
            pixel.red = o_pixel.red
            pixel.green = o_pixel.green
            pixel.blue = o_pixel.blue
    return new_img


def collage(img1, img2, img3, img4, thickness):
    width = img1.width * 2 + thickness * 3
    height = img1.height * 2 + thickness * 3
    collage_img = Image.blank(width, height)
    for y in range(height):
        for x in range(width):
            pixel = collage_img.get_pixel(x, y)
            pixel.red = pixel.green = pixel.blue = 0
    collage_img = framed(collage_img, img1, thickness, thickness)
    collage_img = framed(collage_img, img2, (2*thickness + img1.width), thickness)
    collage_img = framed(collage_img, img3, thickness, (2*thickness + img1.height))
    collage_img = framed(collage_img, img4, (2*thickness + img1.width), (2*thickness + img1.height))
    return collage_img


def detect_green(pixel, threshold, factor) -> bool:
    average = (pixel.red + pixel.green + pixel.blue) / 3
    return pixel.green >= factor * average and pixel.green > threshold


def greenscreen(foreground, background, threshold, factor):
    final = Image.blank(background.width, background.height)
    for y in range(background.height):
        for x in range(background.width):
            fp = final.get_pixel(x, y)
            bp = background.get_pixel(x, y)
            fp.red = bp.red
            fp.green = bp.green
            fp.blue = bp.blue
    for y in range(foreground.height):
        for x in range(foreground.width):
            fp = foreground.get_pixel(x, y)
            if not detect_green(fp, threshold, factor):
                np = final.get_pixel(x, y)
                np.red = fp.red
                np.green = fp.green
                np.blue = fp.blue
    return final


def main(args: list):
    if validate_commands(args):
        print("Command line arguments are valid.")
        if args[0] == "-d":
            Image(args[1]).show()  # display's the image
        elif args[0] == "-k":
            darken(Image(args[1]), float(args[3])).save(args[2])
        elif args[0] == "-s":
            sepia(Image(args[1])).save(args[2])
        elif args[0] == "-g":
            grayscale(Image(args[1])).save(args[2])
        elif args[0] == "-b":
            make_borders(Image(args[1]), int(args[3]), args[4], args[5], args[6]).save(args[2])
        elif args[0] == "-f":
            flipped(Image(args[1])).save(args[2])
        elif args[0] == "-m":
            mirror(Image(args[1])).save(args[2])
        elif args[0] == "-c":
            collage(Image(args[1]), Image(args[2]), Image(args[3]), Image(args[4]), int(args[6])).save(args[5])
        elif args[0] == "-y":
            greenscreen(Image(args[1]), Image(args[2]), float(args[4]), float(args[5])).save(args[3])
        elif args[0] == "-h":
            print("-d: displays image\n"
                  "-k: darkens image\n"
                  "-s: sepia filter\n"
                  "-g: grayscale filter\n"
                  "-b: gives an image borders\n"
                  "-f: flips image\n"
                  "-m: mirrors image\n"
                  "-c: collages four images\n"
                  "-y: combines greenscreen image w/ background")
    else:
        print("Invalid command line arguments.")


if __name__ == "__main__":
    main(sys.argv[1:])

# run pytest with: python3 -m pytest -vv .
# doctests: python3 -m doctest image_processing.py
