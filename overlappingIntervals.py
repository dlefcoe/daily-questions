'''

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

tups = [(30, 75), (0, 50), (60, 150)]

def intervalsFuntion(arrOFtuples):
    
    # for i in tups:
    #     print(i)
    
    # # sort by start time
    tupsSort = sorted(tups, key=lambda x:x[1])
    
    # for each tuple a parllel exists if the start begins before the end finishes.
    overlaps = 1
    for i, tp in enumerate(tupsSort):
        print(i, tp)
        for j, tp1 in enumerate(tupsSort):
            # only compare if j > i
            if j > i:
                # compare the end point of i to the start point of j
                if tupsSort[i][1] > tupsSort[j][0]:
                    # an overlap is found
                    overlaps += 1
            else:
                overlaps = overlaps + 0
                pass

    print('number of overlaps:',overlaps)


'''
The above did not resolve. It will overcount due to level.
Therefore, need a new element in the tuple corresponding to a level and only compare values on the same levels.
or can use an array with a tuple => [[level=1, (0,50)] , [level=2, (30,75)], [level=1, (60,150)]]
max level = 2

sort into bucket levels

level 2 =    (30,75)   <---- this is raised to a level 2
level 1 = (0,50) (60,150) <--- this falls back into a level 1

then count the number of levels

'''



if __name__ == "__main__":
    intervalsFuntion(tups)

    pass


