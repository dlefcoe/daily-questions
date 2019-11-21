'''



'''




from random import randint

class Matrix:
    """Class to represent a matrix."""
    def __init__(self, width, height, weighting):
        """Generate a random matrix of 1s and 0s.
        Weighting is an int between 0 and 100 to determine ratio
        of 1's."""

        self.width = width
        self.height = height
        self.memo = {}
        self.matrix = []

        for x in range(height):
            row = []

            for y in range(width):
                row.append(0 if randint(1, 100) > weighting else 1)

            self.matrix.append(row)

        self.matrix = [[1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0]]

        self.matrix = [[1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,0,0,0,0,0],
                        [1,1,1,0,0,0],
                        [1,0,1,0,0,0],
                        [1,1,1,0,0,0]]

        self.matrix = [[0,0,0,0,0,0],
                        [0,1,1,1,1,0],
                        [0,0,1,1,0,0],
                        [0,0,1,1,0,0],
                        [0,0,1,0,0,0],
                        [0,0,1,0,0,0]]
                        
    def __repr__(self):
        """Print the matrix."""
        out = ""

        for row in self.matrix:
            out += str(row) + "\n"

        return out

    def get(self, x, y):
        """Return previously encountered value, otherwise store it."""
        if (x, y) not in self.memo:
            self.memo[(x, y)] = self.matrix[y][x]

        return self.memo[(x, y)]

    def is_rectangle(self, x0, y0, x1, y1):
        """Determine whether all in range are 1's. Return area if true."""
        y_orig, x_orig = y0, x0

        while x0 <= x1:
            y0 = y_orig

            while y0 <= y1:
                if not self.get(x0, y0):
                    return False

                y0 += 1
            x0 += 1

        area = (1 + x1 - x_orig) * (1 + y1 - y_orig)
        return area, x_orig, y_orig, x1, y1

    def maxyx(self, x, y):
        """Return number of consecutive 1's across and down."""
        across = down = 1

        while x + across < self.width and self.get(x + across, y):
            across += 1

        while y + down < self.height and self.get(x, y + down):
            down += 1

        return across, down

    def scan(self):
        """Get each element of matrix that is a 1."""
        for y in range(self.height):
            for x in range(self.width):

                if self.get(x, y):
                    yield(x, y)

    def find_biggest(self, x, y):
        """Get largest rectangle starting at x, y."""
        # First get maximum consecutives across and down
        xmax, ymax = self.maxyx(x, y)
        largest_area = 1 # largest area is the initial 1 item
        # if xmax or ymax is 1, ymax or xmax is the largest area
        if min(xmax, ymax) == 1:
            largest_area = max(xmax, ymax)

        # find largest 2d rectangle
        else:
            for scan_x in range(x, x + xmax):
                for scan_y in range(y, y + ymax):
                    if self.is_rectangle(x, y, scan_x, scan_y):
                        area = (1 + scan_y - y) * (1 + scan_x - x)

                        if area > largest_area:
                            largest_area = area

        return largest_area

    def get_largest_rectangle(self):
        """Get coords and size of largest rectangles."""
        biggest = 0
        position = None

        for coord in self.scan():
            best = self.find_biggest(*coord)

            if best > biggest:
                biggest = best
                position = coord

        # Return values as 1-indexed instead of 0 indexed to make more readable
        # position = map(lambda x: x + 1, position)
        return biggest, tuple(position)


# Create a 6 x 6 matrix with approx 55% ratio of 1 to 0
m = Matrix(6, 6, 55)
print(m) # print the matrix
biggest, position = m.get_largest_rectangle()
print(f"Found largest area of {biggest} starting at {position}")


