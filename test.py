'''



'''

def gray(n):
    """Generate gray code."""
    result = ["0", "1"]

    while n > 1:
        new = reversed(result)
        result = ["0" + x for x in result] + ["1" + x for x in new]
        n -= 1

    return result

for line in gray(5):
    print(line)