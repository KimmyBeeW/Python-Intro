from random import randint


def in_range1(n):
    """Write a function that checks to see if n is
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    if n in range(1, 101):
        return True
    else:
        print(f'Bad number: {n}')
        return False


def main():
    """Write code in the main function that generates 1000
    random numbers between 1 and 101 and calls the generated
    function to validate the number generated."""
    for i in range(1000):
        num = randint(1, 101)
        try:
            if not in_range2(num):
                print(f"Bad number: {num}")
        except ValueError as e:
            print(f'Number {num} out of range. Error: {type(e)}.')


def in_range2(num):
    """Redo in_range1, but throw an exception instead of
    throwing false
    """
    if num in range(1, 101):
        return True
    else:
        raise ValueError
