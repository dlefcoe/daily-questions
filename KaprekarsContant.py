'''

The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property:
for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. 
The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.


'''


import collections
import statistics

import matplotlib.pyplot as plt


startNum = int(input('enter a 4 digit number: '))
contant = 6174

def Kaprekar(n):
    '''
    take a number n and do a Kaprekar process

    inputs:
        n: an interger number to be processed

    return: the number of iterations
    '''

    # is the number 4 digits
    if n >= 1000 and n <= 9999:
        pass
        #print('acceptable number')
    else:
        return 'number needs to be 4 digits'
    
    # check for two distinct digits
    numAsList = str(n)
    counter=collections.Counter(numAsList)
    if counter.most_common(1)[0][1] > 2:
        #print('the number', counter.most_common(1)[0][0], 'occurs too frequently')
        return 'needs more distinct numbers'

    
    # now do the processing

    # lets do 10 loops
    for i in range(10):
        ascending = sorted(numAsList)
        ascending = int(''.join(ascending))
        descending = sorted(numAsList, reverse=True)
        descending = int(''.join(descending))

        #print('the new number:',descending-ascending)
        processedNumber = descending - ascending

        # check if processed number = contant
        if processedNumber == contant:
            # return f'result found after {i+1} iterations'
            return i+1
        else:
            numAsList = str(processedNumber)
    


    return 'should never get here'
    


result = Kaprekar(startNum)
print(result)


# okay, lets loop through every number
print('running the loop...')
resultsSet = []
for i in range(1000,9999):
    dataPoint = Kaprekar(i)

    # clean the data for numbers
    if isinstance(dataPoint, int):
        resultsSet.append(dataPoint)

#print(resultsSet)

print('number of results:', len(resultsSet))
print('the least iterations:', min(resultsSet))
print('the most iterations:', max(resultsSet))
print('the average iterations:', round(statistics.mean(resultsSet),3))
print('the stdev iterations:', round(statistics.stdev(resultsSet),3))


plt.hist(resultsSet, density=False, bins=max(resultsSet))  # `density=False` would make counts
plt.ylabel('frequency')
plt.xlabel('number of iterations')
plt.show()

