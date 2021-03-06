
'''
This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. 
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?

'''



def intSwap(inVal):

    # convert to list of integers
    inVal = [ int(x) for x in inVal ]

    # new list for answer
    outVal = []

    for i,v in enumerate(inVal):
        # miss all the evens
        if i%2 == 0:
            continue

        # do the swap into new list
        outVal.append(v)
        outVal.append(inVal[i-1])
    return outVal

# test first one
input = '10101010'
result = intSwap(input)
print(result)

# test second one
input = '11100010'
result = intSwap(input)
print(result)



# multiline method using list comprehension
def multiLineMethod(inVal):
    #outVal = [int(b), int(a) for a, b in zip(inVal[x for x in inVal if int(x)%2==0], [x for x in inVal if int(x)%2!=0])]
    evens = [int(v) for x, v in enumerate(inVal) if int(x)%2==0]
    odds = [int(v) for x, v in enumerate(inVal) if int(x)%2!=0]
    r = [(b,a) for a,b in list(zip(evens, odds))]
    # list of tuples back to list
    r1 = [item for t in r for item in t] 
    return r1

# test the multiline list comprehension method
input = '10101010'
input = '11100010'
result = multiLineMethod(input)
print(result)



# this is for the bonus points
def singleLineMethod(inVal):
    r1 = [item for t in [(b,a) for a,b in list(zip([int(v) for x, v in enumerate(inVal) if int(x)%2==0], [int(v) for x, v in enumerate(inVal) if int(x)%2!=0]))] for item in t]
    return r1

# test the one line method
input = '10101010'
result = singleLineMethod(input)
print(result)



# short sweet one line method for the real bonus points
def shortSweet(inVal):
    #outVal = [inVal[i+1] for i,v in enumerate(inVal) if i%2==0]
    outVal = [inVal[i+1] if i%2==0 else inVal[i-1] for i,v in enumerate(inVal)]
    
    return outVal

input = '10101010'
result = shortSweet(input)
print(result)

# done


