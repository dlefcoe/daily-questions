


def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    for i, val in enumerate(A):
        if i == 0:
            continue
        # compare adjacent elements
        if A[i+1] - A[i] > 1:
            return A[i]+1
    return 'done'



A = [1, 3, 6, 4, 1, 2]


result = solution(A)
print(result)


