import pytest
from lab10 import *

# Write your test code here for Q1


def test_product():
    # If n is greater than or equal to one, compute 1 · 2 · ... · n
    assert product(5) == 120
    assert product(4) == 24
    assert product(3) == 6
    # If n is less than the one or not an integer, raise a ValueError
    with pytest.raises(ValueError):
        product(0)
    with pytest.raises(ValueError):
        product(-1)
    with pytest.raises(ValueError):
        product(0.5678)
    with pytest.raises(ValueError):
        product(-1)
        pytest.fail(f"product(-1) didn't raise an exception")
    with pytest.raises(ValueError):
        product(9.657)
        pytest.fail(f"product(9.657) didn't raise an exception")


def test_summation():
    assert summation(3) == 6
    assert summation(5) == 15
    assert summation(1) == 1
    with pytest.raises(ValueError):
        summation(-1)
    with pytest.raises(ValueError):
        summation(0.5678)


# Q2
#####################################

def test_square():
    # Valid
    assert square(4) == 16
    assert square(3.1415) == 9.86902225
    assert square(5) == 25
    # Border
    assert square(-10) == 100
    # Invalid
    assert square(5) != 10


def test_sqrt():
    # Valid
    assert sqrt(16) == 4
    assert sqrt(9) == 3
    # Border
    assert sqrt(2) == pytest.approx(1.4142135, 0.00001)
    # Invalid (doesn't really work for lamda functions)
    # with pytest.raises(ValueError):
    #     sqrt(-4)


def test_mean():
    # Valid
    assert mean([1, 2, 3, 4, 5, 6]) == 3.5
    assert mean([6, 5, 4, 4, 5, 6]) == 5
    assert mean([11, 12, 13, 14, 15, 16]) == 13.5
    assert mean([14, 17, 29, 4, 3, 10, 34]) == pytest.approx(15.85714, 0.001)
    # Border
    assert mean([1]) == 1
    # Invalid
    with pytest.raises(AssertionError):
        mean(0)
    with pytest.raises(AssertionError):
        mean([])


def test_median():
    # Valid
    assert median([11, 12, 13, 14, 15, 16]) == 13.5
    assert median([1, 2, 3, 4, 5, 6, 7]) == 4
    assert median([14, 17, 29, 4, 3, 10, 34]) == 14
    assert median([14, 17, 29, 4, 3, 34]) == 15.5
    # Border
    assert median([1]) == 1
    assert median([4, 7, 3, 1, 2, 6, 5]) == 4
    # Invalid
    with pytest.raises(AssertionError):
        median(0)
    with pytest.raises(AssertionError):
        median([])


def test_mode():
    # Valid
    assert mode([1, 2, 2, 4, 5, 6]) == 2
    assert mode([3, 6, 7, 9, 2, 4, 3, 5, 3]) == 3
    # Border
    assert mode([1]) == 1
    assert mode([2, 3, 2, 3, 2, 3, 4]) == 2
    # Invalid
    with pytest.raises(AssertionError):
        mode(0)
    with pytest.raises(AssertionError):
        mode([])


def test_std_dev():
    # Valid
    assert std_dev([14, 17, 29, 4, 3, 34]) == pytest.approx(11.596, 0.001)
    assert std_dev([14, 17, 29, 4, 3, 10, 34]) == pytest.approx(10.999, 0.001)
    assert std_dev([65, 34, 97, 24, 34, 33, 59, 40, 11, 24, 3, 7]) == 25.76644566528768
    # Border
    assert std_dev([1]) == 0
    # Invalid
    with pytest.raises(AssertionError):
        std_dev(0)
    with pytest.raises(AssertionError):
        std_dev([])


def test_stat_analysis():
    # Valid
    lst = [65, 34, 97, 24, 34, 33, 59, 40, 11, 24, 3, 7]
    assert stat_analysis(lst) == {"mean": 35.916666666666664, "median": 33.5, "mode": 34, "std_dev": 25.76644566528768}
    # Border
    assert stat_analysis([1]) == {"mean": 1.0, "median": 1.0, "mode": 1, "std_dev": 0}
    # Invalid
    with pytest.raises(AssertionError):
        stat_analysis(0)
    with pytest.raises(AssertionError):
        stat_analysis([])


# OPTIONAL
#####################################

def test_accumulate():
    assert accumulate(add, 0, 3) == 6  # 0 + 1 + 2 + 3
    assert accumulate(add, 2, 3) == 8  # 2 + 1 + 2 + 3
    assert accumulate(mul, 2, 4) == 48  # 2 * 1 * 2 * 3 * 4
    assert accumulate(mul, 3, 7) == 15120  # 3 * 1 * 2 * 3 * 4 * 5 * 6 * 7
    with pytest.raises(ValueError):
        accumulate(add, 5.4, 2.3)
    with pytest.raises(ValueError):
        accumulate(add, 4, 7.2)
    with pytest.raises(ValueError):
        accumulate(add, 4.6, 7)
    with pytest.raises(ValueError):
        accumulate(add, 2.4, 5.3)
    with pytest.raises(ValueError):
        accumulate(mul, 5, 0)  # Raises a ValueError
    with pytest.raises(AssertionError):
        accumulate(4, 0, 5)  # Raises an AssertionError


def test_product_short():
    assert product_short(3) == 6
    assert product_short(5) == 120
    assert product_short(1) == 1
    with pytest.raises(ValueError):
        product_short(0)
    with pytest.raises(ValueError):
        product_short(-1)
    with pytest.raises(ValueError):
        product_short(0.5678)


def test_summation_short():
    assert summation_short(3) == 6
    assert summation_short(5) == 15
    assert summation_short(1) == 1
    with pytest.raises(ValueError):
        summation_short(-1)
    with pytest.raises(ValueError):
        summation_short(0.5678)


def test_invert():
    assert invert(3, 1) == 1/3
    assert invert(1, 1) == 1
    assert invert(0.5, 1) == 1
    with pytest.raises(ZeroDivisionError):
        invert(0, 1)
    with pytest.raises(ValueError):
        invert("potato", 1)
    with pytest.raises(ValueError):
        invert(1, "potato")


def test_change():
    assert change(3, 1, 0.99) == 2/3
    assert change(1, 1, 0.99) == 0
    assert change(0.5, 2, 0.99) == 0.99
    with pytest.raises(ZeroDivisionError):
        change(0, 1, 1)
    with pytest.raises(ValueError):
        change("potato", 1, 1)
    with pytest.raises(ValueError):
        change(1, "potato", 1)
    with pytest.raises(ValueError):
        change(1, 1, "potato")


def test_invert_short():
    assert invert_short(3, 1) == 1 / 3
    assert invert_short(1, 1) == 1
    assert invert_short(0.5, 1) == 1
    with pytest.raises(ZeroDivisionError):
        invert_short(0, 1)
    with pytest.raises(ValueError):
        invert_short("potato", 1)
    with pytest.raises(ValueError):
        invert_short(1, "potato")


def test_change_short():
    assert change_short(3, 1, 0.99) == 2 / 3
    assert change_short(1, 1, 0.99) == 0
    assert change_short(0.5, 2, 0.99) == 0.99
    with pytest.raises(ZeroDivisionError):
        change_short(0, 1, 1)
    with pytest.raises(ValueError):
        change_short(1, 1, "potato")
