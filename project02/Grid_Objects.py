"""Kimberly Williams, Project 02"""
from Particle import Particle


class Sand(Particle):
    def is_move_ok(self, x_to, y_to):
        """needs two parameters, the x and y coordinates that you want to
        try to move to (x_to, and y_to) from the original version."""
        if self.grid.in_bounds(x_to, y_to) and self.grid.get(x_to, y_to) is None:  # if space is inbounds and empty,
            if (((x_to == self.x + 1 or x_to == self.x - 1) and self.grid.get(x_to, self.y) is None)
                    or self.x == x_to):  # if it's moving down to the right or left and the space above it is empty,
                return True  # or if it's simply moving down, return True
        else:
            return False  # else it can't move

    def physics(self):
        if self.is_move_ok(self.x, self.y + 1):  # check down
            return self.x, self.y + 1  # move
        if self.is_move_ok(self.x - 1, self.y + 1):  # check left down
            return self.x - 1, self.y + 1  # move
        if self.is_move_ok(self.x + 1, self.y + 1):  # check right down
            return self.x + 1, self.y + 1  # move


class Rock(Particle):
    """rocks don't move"""
    def physics(self):
        return None


class Bubble(Particle):
    def is_move_ok(self, x_to, y_to):  # same as is_move_ok in Sand
        """needs two parameters, the x and y coordinates that you want to try to
        move to (x_to, and y_to) from the original version."""
        if self.grid.in_bounds(x_to, y_to) and self.grid.get(x_to, y_to) is None:  # if space is inbounds and empty,
            if (((x_to == self.x + 1 or x_to == self.x - 1) and self.grid.get(x_to, self.y) is None)
                    or self.x == x_to):  # if it's moving to the right or left and the space above it is empty,
                return True  # or if it's simply moving up, return True
        else:
            return False  # else it can't move

    def physics(self):
        """
        bubble object will first try to move straight up, then diagonally up and to
        the right, then diagonally up and to the left. If all movements are blocked,
        the physics() method should return None
        """
        if self.is_move_ok(self.x, self.y - 1):  # check up
            return self.x, self.y - 1  # move
        if self.is_move_ok(self.x + 1, self.y - 1):  # check right up
            return self.x + 1, self.y - 1  # move
        if self.is_move_ok(self.x - 1, self.y - 1):  # check left up
            return self.x - 1, self.y - 1  # move
        return None
