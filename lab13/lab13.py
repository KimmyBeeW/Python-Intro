def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n < 2:
        return 1
    else:
        return n * skip_mul(n - 2)


def multiply(m, n):
    """ Takes two positive integers (including zero) and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    return 0 if n == 0 else m + multiply(m, n-1)
    # return 0 if m == 0 else n + multiply(m-1, n)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def prime_helper(num, factor):
        if num == factor:
            return True
        else:
            return num % factor != 0 and prime_helper(num, factor+1)
    return prime_helper(n, 2)


##################################
# Extra practice
def is_prime_iteration(n):  # extra
    """Returns True if n is a prime number and False otherwise.
    Doctests: # python -m doctest lab13.py
    >>> is_prime_iteration(2)
    True
    >>> is_prime_iteration(16)
    False
    >>> is_prime_iteration(521)
    True
    """
    tf = None
    if n == 1 or n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                tf = True
        return tf

def hailstone_iteration(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    Doctests: # python -m doctest lab13.py
    >>> a = hailstone_iteration(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
        elif n % 2 == 1:
            n = int(n*3+1)
        seq.append(n)
    for i in range(len(seq)):
        print(seq[i])
    return len(seq)


def hailstone_recursion(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    Doctests: # python -m doctest lab13.py
    >>> a = hailstone_recursion(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    seq = [n]
    print(n)

    def helper(num, seq1):
        if num == 1:
            return len(seq1)
        else:
            if num % 2 == 0:
                num = int(num / 2)
            elif num % 2 == 1:
                num = int(num * 3 + 1)
            print(num)
            seq1.append(num)
            return helper(num, seq1)
    return helper(n, seq)


def paths_iteration(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    Doctests: # python -m doctest lab13.py
    >>> paths_iteration(2, 2)
    2
    >>> paths_iteration(5, 7)
    210
    >>> paths_iteration(117, 1)
    1
    >>> paths_iteration(1, 157)
    1
    """
    # C(M+N−2,M−1)
    a = m+n-2
    b = m-1
    numer = 1
    denominator = 1
    for i in range(2, a+1):
        numer *= i
    for j in range(2, (a-b)+1):
        denominator *= j
    for k in range(2, b+1):
        denominator *= k
    return int(numer/denominator)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    Doctests: # python -m doctest lab13.py
    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    def factorial(num):
        return 1 if num == 0 or num == 1 else num * factorial(num - 1)
    a = m + n - 2
    b = m - 1
    return int(factorial(a)/(factorial(b)*factorial(a-b)))  # C(M+N−2,M−1)


# if __name__ == "__main__":
    # z = hailstone_recursion(10)
    # print(z)
