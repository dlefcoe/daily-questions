import itertools as it
import random
import time

# some population cases
population = [30, 100, 200, 150, 80, 40, 100, 100, 100, 100, 90]
population = [10, 10, 10, 10, 10, 180, 180, 180, 180, 180]
population = [100, 200, 150, 80]

population = [random.randint(1,200) for x in range(100)]
boatLimit = 200


def rescue(population, boatLimit, numBoats, keep_going=True):
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
        # find valid pairs
        if i[0]+i[1] <= boatLimit:
            viablePairs.append(i)
    
    # print('reductions made, the size left:', len(viablePairs))

    if len(viablePairs)==0:
        #print('no viable pairs')
        numBoats = numBoats + len(population)
        print('the number of boats:',numBoats)
        keep_going = False

    else:
        # remove pair
        population.remove(viablePairs[0][0])
        population.remove(viablePairs[0][1])
        numBoats = numBoats + 1
    
    return population, boatLimit, numBoats, keep_going



t1 = time.time()
# rescue(population, boatLimit, 0)
numBoats = 0
keep_going = True    
while keep_going:
    population, boatLimit, numBoats, keep_going = rescue(population, boatLimit, numBoats)

t2 = time.time()
print('time taken:', round(t2-t1, 3), 'seconds')

