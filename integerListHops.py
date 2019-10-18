'''


This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, 
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.



'''




def intListHop(a):
    # get the first value

    subtractor = a[0]
    
    for i, v in enumerate(a):
        if i == 0:
            continue
        subtractor = subtractor - v
        if subtractor < 0:
            # run out of hops
            val = False
        else:
            val = True

    return val



a = [2, 0, 1, 0]
print(intListHop(a))

b = [1, 1, 0, 1]
print(intListHop(b))



# ==============================================
# this is the working version
# ==============================================






def solve(a):
    if len(a) == 1:
        return True

    elif a[0] == 0:
        return False

    elif len(a) <= a[0]:
        return False

    return solve(a[a[0]:])


goods = (
    [2, 0, 1, 0],
    [3, 2, 1, 1],
    [2, 5, 4, 9, 9, 9, 1, 0],
)

bads = (
    [1, 1, 0, 1],
    [6, 3, 2],
    [2, 6, 2, 3, 0, 1]
)

for x in goods + bads:
    print(solve(x))