'''
The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. 
They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.

Write a function that prints out all the steps necessary to complete the Tower of Hanoi. #
You should assume that the rods are numbered, with the first rod being 1, 
the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3


'''


class IllegalMoveException(Exception):
    def __init__(self, source, dest):
        print(f"Illegal Move from {source.name}: {source} to {dest.name}: "
              f"{dest}")

class Tower(list):
    """Class to represent a tower."""
    # This is just a list
    def __init__(self, name, iterable=None):
        """Initialise as list and set a name."""
        self.name  = name
        super(Tower, self).__init__()
        self.extend(iterable or [])

    @property
    def is_empty(self):
        """Return whether tower has zero blocks."""
        return self.__len__() == 0

    @property
    def top(self):
        """Get the top block."""
        return self[-1] if not self.is_empty else 0

class Hanoi:
    """Class to represent a with n blocks game."""
    def __init__(self, height=5):
        """Initialise a game with 'height' number of blocks."""
        self.a = Tower("a", (x for x in range(height, 0, -1)))
        self.b = Tower("b")
        self.c = Tower("c")
        self.cols = (self.a, self.b, self.c)
        self.history = []

    def __repr__(self):
        """Override print function to show contents of the three towers."""
        out = ""
        for c in self.cols:
            out += str(c) + "\n"
        return f"---\n{out}\n---"

    def move(self, source, dest):
        """Perform a block move from one tower to another, if legal."""
        if not source.is_empty:

            # Ensure the move is legal
            if dest.top > source.top or dest.is_empty:
                dest.append(source.pop())

                # Add move to log
                self.history.append((source.name, dest.name))

            else:
                # Raise exception and exit if illegal move attempted
                raise IllegalMoveException(source, dest)

    def get_possible_moves(self):
        """Get all possible moves."""
        legal = []
        for source in self.cols:

            # Ensure source is not empty
            if not source.is_empty:

                for dest in game.cols:
                    # Ensure dest is not source
                    if dest is not source:

                        # Ensure move is legal
                        if dest.top > source.top or dest.is_empty:

                            # Ensure this doesn't undo the last move
                            if not len(self.history) or \
                                    self.history[-1] != (dest.name, source.name):

                                # Add move to list of legal moves
                                legal.append((source, dest))

        return legal


import time
import random
height = 2

game = Hanoi(height)
print(game)
while len(game.b) < height:
    pm = game.get_possible_moves()
    rand = random.choice(pm)
    game.move(*rand)
print(f"completed game in {len(game.history)} moves!")
print(game)