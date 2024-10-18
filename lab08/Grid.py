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
            print("Out of bounds.")
            return False

    def get(self, x, y):
        """Gets the value stored value at (x, y).
        (x, y) should be in bounds."""
        if self.in_bounds(x, y):
            return self.array[y][x]

    def set(self, x, y, val):
        """Sets a new value into the grid at (x, y).
        (x, y) should be in bounds."""
        if self.in_bounds(x, y):
            self.array[y][x] = val
        return None

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        else:
            return False
