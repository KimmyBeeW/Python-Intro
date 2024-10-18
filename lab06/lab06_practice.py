import sys


def main(args):
    """
    Valid flags:
    -p : prints out all the command line arguments after the -p
    -i : prints "Hello World"
    -h : prints out a help command
    """
    valid_flags = ["-p", "-i", "-h"]
    for item in args:
        if item not in valid_flags:
            # print("Not a valid flag")
            break
        else:
            pass


if __name__ == "__main__":
    main(sys.argv[1:])

