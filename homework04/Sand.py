from Particle import Particle


class Sand(Particle):
    def __str__(self):
        return f"Sand({self.x},{self.y})"

    def is_move_ok(self, x_to, y_to):
        """needs two parameters,
        the x and y coordinates that you want to try to move to (x_to, and y_to) from the original version."""
        if self.grid.in_bounds(x_to, y_to) and self.grid.get(x_to, y_to) is None:  # if space is inbounds and empty,
            if (((x_to == self.x + 1 or x_to == self.x - 1) and self.grid.get(x_to, self.y) is None)
                    or self.x == x_to):  # if it's moving down to the right or left and the space above it is empty,
                return True              # or if it's simply moving down, return True
        return False                 # else it can't move

    def physics(self):
        if self.is_move_ok(self.x, self.y + 1):  # check down
            return self.x, self.y + 1  # move
        if self.is_move_ok(self.x - 1, self.y + 1):  # check left down
            return self.x - 1, self.y + 1  # move
        if self.is_move_ok(self.x + 1, self.y + 1):  # check right down
            return self.x + 1, self.y + 1  # move
        return None

    # def gravity(self):  # NOT NECESSARY FOR THIS HOMEWORK. Just leftover from former class
    #     """This is similar to the do_gravity() function from Part 1 of the Sand Project; however, instead of actually
    #     moving the sand particle in the grid, it just returns the position the sand particle should move to.
    #     This method doesn't take any parameters and returns a tuple containing the x and y coordinates that the
    #     particle should move to. If there is no valid position to move to, the method should return None."""
    #     if isinstance(self.grid.get(self.x, self.y), Sand):
    #         if self.is_move_ok(self.x, self.y + 1):
    #             x_to = self.x
    #             y_to = self.y + 1
    #             return x_to, y_to
    #         elif self.is_move_ok(self.x - 1, self.y + 1):
    #             x_to = self.x - 1
    #             y_to = self.y + 1
    #             return x_to, y_to
    #         elif self.is_move_ok(self.x + 1, self.y + 1):
    #             x_to = self.x + 1
    #             y_to = self.y + 1
    #             return x_to, y_to
    #     else:
    #         return None