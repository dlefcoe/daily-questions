/**
 * 
 * inspection of covid 19 data
 * 
*/



let coronaData = {
    numberOfCases : 2000000,
    totalDeaths : 100000,
    recoveries : 375000,
    todaysDeaths : 300,
    totalDailyCases : 300000
}



/**
 * @class for world population
 */
class worldpopulation{
    constructor(){
        this.population = 8000000000
        this.birthsToday = 250000
        this.deathsToday = 100000
        this.populationGrowth = this.birthsToday - this.deathsToday
    }

    doSomething(params) {
        console.log(`hello ${params}`)    
    }

    killPopulation(num){
        this.population = this.population - num
    }

}


let wp = new worldpopulation()

wp.doSomething('darren')

console.log(wp.birthsToday)

console.log(coronaData.numberOfCases)


console.log(wp.population)
wp.killPopulation(1000000000)
console.log(wp.population)



