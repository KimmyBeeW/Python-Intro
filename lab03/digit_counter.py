def digit_counter(func, num):
    """Return the number of digits when func(num) is true"""
    counter = 0
    while num > 0:  # change 1 >= to >
        print(f'if statement: {num} % 10 = {num % 10}')
        if func(num % 10):
            counter += 1
        num = num // 10  # change 2 pull out of if statement
        print(f'num = {num}')
    print(f'counter = {counter}')
    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


"""ADD_TESTING_CODE"""
digit_counter(is_even, 1112)
