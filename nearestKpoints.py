
'''
Given a list of points, a central point, and an integer k, 
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], 
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].

'''




def pythag(a, b):
    """Pythagoras using two co-ords."""
    sides = a[0] - b[0],  a[1] - b[1]
    return (sum(s ** 2 for s in sides)) ** 0.5

def nearest(points, central, k):
    """Return k nearest points to central."""
    distances = {p: pythag(central, p) for p in points}
    return sorted(distances, key=distances.get)[:k]

points = ((0, 0), (5, 4), (3, 1))
answer = nearest(points, (1, 2), 2)
print(answer)



