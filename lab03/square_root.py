def square_root(num):
    """Calculate the square root with 0.000001 precision"""
    num = abs(num)

    low = 0
    high = num
    middle = num
    old_middle = -1
    iteration_count = 0

    accuracy = 0.000001  # fix2
    while abs(old_middle - middle) > accuracy:  # fix1
        old_middle = middle

        middle = (high + low) / 2  # fix3
        middle_squared = middle ** 2  # fix5

        if middle_squared < num:  # fix4
            low = middle
        else:
            high = middle

        iteration_count += 1

    return round(middle, 4), iteration_count  # fix6


# Testing code
print(square_root(9))
print(square_root(8))
