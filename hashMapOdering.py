'''
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values,
which represents that the prerequisites of courseId are courseIds. 
 
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, 
should return ['CSC100', 'CSC200', 'CSCS300'].

'''



def sortCourseId(courseId):
    # new array
    a = []

    # create list of tuples from dict
    for k in courseId:
        v = k, len(courseId[k])
        a.append(v)
    
    # sort by second item in tuple
    a.sort(key=lambda x: x[1])
    
    # reduce to single items
    b = [b[0] for b in a]

    return b


courseId = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}

result = sortCourseId(courseId)
print(result)


