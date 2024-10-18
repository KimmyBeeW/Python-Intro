from operator import add, mul


def product(n):
    """
    takes in an integer parameter n. product returns the result of 1 · 2 · 3 · ... · n;
    however, if n is less than one or not an integer, raise a ValueError.
    >>> product(5)
    120
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Please only use positive integers")
    else:
        total = 1
        for i in range(1, n+1):
            total = total * i
        return total


def summation(n):
    """takes in an integer parameter n.
    summation returns the result of 1 + 2 + ... + n;
    however, if n is less than zero or not an integer, raise a ValueError."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Please only use positive integers")
    else:
        total = 0
        for i in range(1, n+1):
            total += i
        return total


#############################################
# Q2

square = lambda x: x * x  # change + to *

sqrt = lambda x: x ** 0.5  # x^0.5 == √x


def mean(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"
    
    total = 0
    for num in numbers:
        total += num

    return total / len(numbers)  # delete double divide


def median(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    numbers = sorted(numbers) 
    # `sorted` returns a sorted list. `sorted` works. 
    if len(numbers) % 2 == 0:
        left_mid = len(numbers) // 2 - 1  # add -1
        right_mid = left_mid + 1
        return mean([numbers[left_mid], numbers[right_mid]])  # left and right mid are indices
    else:
        middle = len(numbers) // 2
        return numbers[middle]


def mode(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    counts = {}
    running_high_num = 0
    counts[running_high_num] = 0
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        
        if counts[num] > counts[running_high_num]:
            running_high_num = num

    return running_high_num


def std_dev(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    avg = mean(numbers)
    total_dist = 0
    for num in numbers:
        total_dist += square(num - avg)

    return sqrt(total_dist / len(numbers))


def stat_analysis(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    info = {}
    info["mean"] = mean(numbers)
    info["median"] = median(numbers)
    info["mode"] = mode(numbers)
    info["std_dev"] = std_dev(numbers)
    return info
    

#############################################
# (OPTIONAL) Write your code here for Accumulate, Invert, and Change
def accumulate(merger, initial, n):
    """accumulate with contain the logic of applying some function merger to initial and to each value in the range from
    one to n. It will then return the total after merger has been applied to each value. (merger will either be the add
    or mul functions.) Additionally, if n is less than the initial or not an integer, raise a ValueError."""
    if not isinstance(n, int) or not isinstance(initial, int) or n < initial:
        raise ValueError("Please only use positive integers for initial and n, and make sure n ≥ initial.")
    elif merger != mul and merger != add:
        raise AssertionError("Functions can only be 'add' or 'mul'.")
    else:
        total = initial
        for i in range(1, n+1):
            total = merger(total, i)
        return total


def product_short(n):
    return accumulate(mul, 1, n)


def summation_short(n):
    return accumulate(add, 0, n)


def invert(x, limit):
    """takes in a number x and limit as parameters. invert calculates 1/x, and if the quotient is less than the limit,
    the function returns 1/x; otherwise the function returns limit. However, if x is zero, the function
    raises a ZeroDivisionError."""
    if x == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    elif not isinstance(x, int) and not isinstance(x, float):
        raise ValueError("x must be a number")
    elif not isinstance(limit, int) and not isinstance(limit, float):
        raise ValueError("Limit must be a number.")
    else:
        quot = 1/x
        if quot < limit:
            return quot
        else:
            return limit


def change(x, y, limit):
    """takes in numbers x, y and limit as parameters and returns abs(y - x) / x if it is less than the limit;
    otherwise the function returns the limit. If x is zero, raise a ZeroDivisionError."""
    if x == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    elif ((not isinstance(x, int) and not isinstance(x, float)) or (not isinstance(y, int) and not isinstance(y, float))
          or (not isinstance(limit, int) and not isinstance(limit, float))):
        raise ValueError("Limit, x, and y must all be numbers")
    else:
        num = abs(y - x) / x
        if num < limit:
            return num
        else:
            return limit


def limited(numerator, denominator, limit):
    if denominator == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    elif ((not isinstance(numerator, int) and not isinstance(numerator, float)) or
          (not isinstance(denominator, int) and not isinstance(denominator, float)) or
          (not isinstance(limit, int) and not isinstance(limit, float))):
        raise ValueError("Limit, numerator, and denominator must all be numbers")
    else:
        val = numerator / denominator
        if val < limit:
            return val
        else:
            return limit


def change_short(x, y, limit):
    return limited(abs(y-x), x, limit)


def invert_short(x, limit):
    return limited(1, x, limit)
