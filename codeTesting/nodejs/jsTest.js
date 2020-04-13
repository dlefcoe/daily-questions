//const prompt = require('prompt');


x = 10
console.log(x)

a = 10, b = 5;
console.log(a, b);
[a, b] = [b, a]
console.log(a,b)


let c = 5, d = 6;
[c, d] = [d, c]
console.log(`${c} ${d}`);


[l,m] = [3,4];
console.log(l, m);

[l,m] = [m,l]
console.log(l,m);


for (let i = 0; i < 10; i++) {
    // do the code in the loop

}

if (l == m) {
    console.log('l == m')    
}else{
    console.log('l != m')
}



rndNumber = Math.random()
console.log(`the random number is ${rndNumber}`)


rndInt = Math.floor(Math.random()*100)
console.log(`the random integer is ${rndInt}`)




// hoisting example

let hoistExample = 10
console.log(`hoist example ${hoistExample}`)


// list comprehension

let testArray = [5,10,15,20,25,30]


let newArrayDouble = []
testArray.forEach(function (elem,index) {
    // newArrayDouble.push(elem*2)  
    newArrayDouble[index] = elem*2  
})
console.log(newArrayDouble)


// ammend the list in place
testArray.forEach((val, index)=>{testArray[index]= val*2})


var doubleArray = [] // declare new array
for (let i of testArray) {
    doubleArray.push(i*2)    
}

console.log(doubleArray)


// testing array things
let newArr = Array(5)

console.log(newArr)

for (const iterator of Array(5)) {
    console.log('hllo', iterator)
}

console.log([...Array(5).keys()])





var numbers = [4, 9, 16, 25];
var xSqrt = numbers.map(Math.sqrt)

console.log(numbers)
console.log(xSqrt)


// make a new array based on an old array
let xOperation = numbers.map((val) =>{
    if (val < 10) {
        return 10
    }
    else return val
})

console.log(xOperation)







