#
# laylee inspection of corona virus
#


class CoronaData:
    ''' infomation about corona data '''
    
    numberOfCases = 2_000_000
    totalDeaths = 100_000
    recoveries = 375_000
    todaysDeaths = 300
    totalDailyCases = 7500


class WorldPopulation:
    ''' information about world population    '''
    
    population = 8_000_000_000
    birthsToday =250_000
    deathsToday = 100_000
    populationGrowth = birthsToday - deathsToday

    def __init__(self):
        self.tryme = 1_000_000


    def killPeople(num):
        WorldPopulation.population = WorldPopulation.population - num



def main():
    ''' this is the main function '''

    # classes to call
    # cd = CoronaData
    # wp = WorldPopulation

    coronaCalcs()

    

def coronaCalcs(cd=CoronaData, wp=WorldPopulation):
    ''' some calcs for corona
    
    inputs:
        cd -- the corona data
        wp -- the world population data


    '''

    print('the world population growth:', wp.populationGrowth)

    # normalise (compare, rationalise, make sense of) the data
    
    # compare corona deaths to world population deaths

    # first method - comparing total deaths to world population
    coronaTotalDeathsToWorldPopulation = cd.totalDeaths / wp.population
    coronaTotalDeathsToWorldPopulation_percent = coronaTotalDeathsToWorldPopulation * 100
    
    print('first method - comparing total deaths to world population')
    print(coronaTotalDeathsToWorldPopulation_percent)


    # second  method - comparing  deaths today to world population deaths today
    coronaToWorldPopulationDeathsToday = cd.todaysDeaths / wp.deathsToday
    coronaToWorldPopulationDeathsToday_percent = coronaToWorldPopulationDeathsToday * 100

    print('second  method - comparing  deaths today to world population deaths today')
    print(coronaToWorldPopulationDeathsToday_percent)

    # killing the world population
    print('killing the world population')
    print(wp.population)
    wp.killPeople(1000000000)
    print(wp.population)

    



main()







