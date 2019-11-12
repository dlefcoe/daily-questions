
'''

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.

'''


class SparseArray:
    """A Sparse Array."""
    def __init__(self, arr, size=None):
        """Create dict of (index, value) for values that are not zero."""
        self.size = size or len(arr)
        self.data = {idx: val for idx, val in enumerate(arr) if val is not 0}

    def set(self, i, val):
        """Set a value."""
        if i > self.size:
            raise IndexError

        if val != 0:
            self.data[i] = val

        if val == 0 and i in self.data:
            del self.data[i]

    def get(self, i):
        """Get a value."""
        if not 0 <= i < self.size:
            raise IndexError

        return self.data.get(i, 0) # returns 0 if key not in dict

arr = [0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 7] + 200 * [0]
sparse = SparseArray(arr, len(arr))
sparse.set(214, 3)  # Update value at index 214 to 3
print(f"internal data    : {sparse.data}")
print(f"effective values : {[sparse.get(x) for x in range(len(arr))]}")

# remove an item of data
sparse.set(214, 0)
print(f"internal data    : {sparse.data}")

