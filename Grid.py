"""Kimberly Williams, Project 2B"""
from copy import deepcopy


class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, height, and array. Initially all locations hold None.
        """
        self.width = width
        self.height = height
        self.array = []
        for i in range(height):
            self.array.append([None]*width)

    def in_bounds(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            # print("Out of bounds.")
            return False

    def get(self, x, y):
        """Gets the value stored value at (x, y).
        (x, y) should be in bounds."""
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            raise IndexError

    def set(self, x, y, val):
        """Sets a new value into the grid at (x, y).
        (x, y) should be in bounds."""
        if self.in_bounds(x, y):
            self.array[y][x] = val
            return None
        else:
            raise IndexError

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid.build({self.array})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other
        else:
            return False

    @staticmethod
    def check_list_malformed(lst):
        """This method verifies that the nest list passed to the build() method is of the correct structure
        (i.e. rectangular) to properly build a grid.
            The object passed in should be a list object
            The top-level list should not be empty
            Each element of the list object should also be a list object
            Each element of the top-level list should have the same length"""
        if lst is None or not isinstance(lst, list):
            print('Grid must be in the form of a list.')
            raise ValueError()
        elif len(lst) == 0 or not isinstance(lst[0], list) or len(lst[0]) == 0:
            print("Grid must be at least 1x1")
            raise ValueError()
        elif len(lst) > 1 and len(lst[0]) != len(lst[1]):
            print("Error in grid mechanism")
            raise ValueError()

    @staticmethod
    def build(lst):
        """this method takes a nested list and turns it into a Grid object."""
        Grid.check_list_malformed(lst)
        height = len(lst)
        width = len(lst[0])
        grid = Grid(width, height)
        grid.array = deepcopy(lst)
        return grid

    def copy(self):
        """returns a copy of the current Grid object"""
        return Grid.build(self.array)
