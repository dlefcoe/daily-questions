'''


An imminent hurricane threatens the coastal town of Codeville.

If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, 
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.


'''

import itertools as it

population = [30, 100, 200, 150, 80, 40, 100]
population = [100, 200, 150, 80]
boatLimit = 200

def rescue(population, boatLimit, numBoats):
    '''
    Take population, limit and return smallest number of boats required

    input:
        population: array on numbers
        limit: number
    return:
        number: smallest number of boats
    '''
    population.sort(reverse=True)
    c = it.combinations(population, 2)

    viablePairs = []
    for i in c:
        # fnd valid pairs
        if i[0]+i[1] <= boatLimit:
            viablePairs.append(i)
    
    print('reductions made:',viablePairs)

    if len(viablePairs)==0:
        #print('no viable pairs')
        numBoats = numBoats + len(population)
        print('the number of boats:',numBoats)

    else:
        # remove pair
        population.remove(viablePairs[0][0])
        population.remove(viablePairs[0][1])
        numBoats = numBoats + 1

        # call function again
        rescue(population, boatLimit, numBoats)
    




rescue(population, boatLimit, 0)



