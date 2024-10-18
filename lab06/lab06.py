import sys


def print_args(args):
    for arg in args:
        print(arg)


def check(args):
    """checks to see, given a list of arguments, if the second argument is one of
    -p, -i, -h, -w, or -r and returns True if it is; otherwise, it returns False."""
    if args[1] in ["-p", "-i", "-h", "-w", "-r"]:
        return True
    else:
        return False


def flags(args):
    """Valid flags:
    -p : prints out all the command line arguments after the -p
    -i : prints "Hello World"
    -h : prints out a help command
    -w : write to a file specified in the next argument with the contents given in the arguments following the file name
    -r : read from the file specified in the following arguments and print out each line in the file"""
    if check(args):
        if args[1] == '-p':
            print_args(args[2:])
        elif args[1] == "-i":
            print('Hello World')
        elif args[1] == "-h":
            print('Valid flags:\n-p : prints out all the command line arguments after the -p\n-i : prints '
                  '"Hello World"\n-h : prints out a help command')
        elif args[1] == "-w":
            if len(args) <= 3:
                print("No Content Provided")
            else:
                new_txt = []
                for arg in args[3:]:
                    new_txt.append(f'{arg}\n')
                with open(args[2], 'w') as out_file:
                    out_file.writelines(new_txt)
        elif args[1] == "-r":
            with open(args[2], 'r') as out_file:
                lines = out_file.readlines()
                for line in lines:
                    print(line.strip())
    else:
        print_args(args)


if __name__ == '__main__':
    the_args = sys.argv
    flags(the_args)
