/**
 * 
 * 
 *  JavaScript arrays
 * 
 * 
 */




let cars = ['saab','volvo','bmw']


let name = cars[0]

console.log(name)

// change an arrary element

cars[0] = 'opel'

console.log(cars)

let person = ["John", "Doe", 46]

console.log(person[0])


let person1 = {firstName:"John", lastName:"Doe", age:46}


console.log(person1.lastName)



let thisArray = [100, person, 'hello world', person1]

console.log(thisArray)

let s = thisArray[3].lastName

console.log(s)

let x = cars.length
console.log('the cars array length:',x)

let y = cars.sort()
console.log(y)

y.reverse()
console.log(y)


let fruits = ["Banana", "Orange", "Apple", "Mango"]


let first = fruits[0]
console.log(first)

let last = fruits[fruits.length-1]
console.log(last)


let fLen = fruits.length

for (let i=0; i<fLen;i++) {
    console.log(fruits[i])
}

// the for each method

console.log('testing the foreach method')
fruits.forEach((fruit)=>{console.log(fruit)})

fruits.push('lemon')

console.log('this is the array with a lemon added')
console.log(fruits)



let myNewArray = []


console.log(myNewArray)

let darren = {
    height: 50,
    weight: 75,
    haircolour:'brown',
    eyeColour:'hazel'
}


