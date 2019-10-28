'''

function to calculate the product of two vectors of length 3.



'''


v1 = [5, 4, 10]
v2 = [1, 9, 3]


def crossProduct(v1, v2):
    ''' multiple 2 vestors [Cross product] '''
    s1 = v1[1]*v2[2] - v1[2]*v2[1]
    s2 = v1[2]*v2[0] - v1[0]*v2[2]
    s3 = v1[0]*v2[1] - v1[1]*v2[0]

    s = [s1, s2, s3]

    return s


answer = crossProduct(v1, v2)
print(answer)



def dotProduct(v1, v2):
    s1 = v1[0]*v2[0]
    s2 = v1[1]*v2[1]
    s3 = v1[2]*v2[2]

    s = s1 + s2 + s3

    return s


def generalDotProduct(v1, v2):
    
    # check for same length
    if len(v1) != len(v2):
        return 'not same lenght'

    # multiple elements
    s = 0
    for i in range(len(v1)):
        s += v1[i]*v2[i]

    return s

answer = dotProduct(v1, v2)
print(answer)


answer = generalDotProduct(v1, v2)
print(answer)


# here is the dot product in 1 line
if len(v1) == len(v2): s = sum([v1[i]*v2[i] for i in range(len(v2))])
print(s)