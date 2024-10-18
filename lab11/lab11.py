from Grid import Grid
from random import random
from copy import deepcopy


def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def random_rocks(grid, chance_of_rock):
    """Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position."""
    rock_grid = deepcopy(grid)
    # for y in range(rock_grid.height):
    #     for x in range(rock_grid.width):
    #         if rock_grid.get(x, y) is None and random() <= chance_of_rock:
    #             rock_grid.set(x, y, "r")
    # return rock_grid
    return modify_grid(rock_grid, lambda x, y: rock_grid.set(x, y, 'r'), chance_of_rock)


def random_bubbles(grid, chance_of_bubbles):
    """Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position."""
    bubble_grid = deepcopy(grid)
    # for y in range(bubble_grid.height):
    #     for x in range(bubble_grid.width):
    #         if bubble_grid.get(x, y) is None and random() <= chance_of_bubbles:
    #             bubble_grid.set(x, y, "b")
    # return bubble_grid
    return modify_grid(bubble_grid, lambda x, y: bubble_grid.set(x, y, 'b'), chance_of_bubbles)


def modify_grid(grid, func, prob):
    """ higher-order function for random_bubbles and random_rocks
    :param grid: copy from bubbles or rocks
    :param func: lambda x,y:
    :param prob: probability
    :return grid: grid object updated by the function passed in
    """
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) is None and random() <= prob:
                func(x, y)
    return grid


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    up_grid = deepcopy(grid)
    # if up_grid.get(x,y)=='b' and up_grid.get(x,y-1) is None and y > 1: # add if not known if bubble can move.
    up_grid.set(x, y, None)
    up_grid.set(x, y-1, 'b')
    return up_grid


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    bubble_grid = deepcopy(grid)
    for y in range(1, grid.height):
        for x in range(grid.width):
            if bubble_grid.get(x, y) == "b" and bubble_grid.get(x, y - 1) is None:
                bubble_grid = bubble_up(bubble_grid, x, y)
    return bubble_grid


def animate_grid(grid, delay):
    """Given a Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    print(message)
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        new_grid = move_bubbles(prev)
        if new_grid == prev:
            break
        prev = new_grid
        count += 1


if __name__ == "__main__":
    grid1 = Grid(50, 10)
    grid1 = random_rocks(grid1, 0.1)
    grid1 = random_bubbles(grid1, 0.2)
    animate_grid(grid1, 0.5)

# python3 -m pytest test_lab11.py::test_random_rocks
# python3 -m pytest -vv .
