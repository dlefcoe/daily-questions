/**
 * 
 *  Objects in nodeJS
 * 
 * @dlefcoe
 * 
 */


console.time("whole code")


// JavaScript Objects

// This code assigns a simple value (Fiat) to a variable named car:
let car = 'fiat'

console.log(car)



// Objects are variables too. But objects can contain many values.
// This code assigns many values (Fiat, 500, white) to a variable named car:


let van = {type:"Fiat", model:"500", color:"white", doesWork:test(100)}
//let van = {type:"Fiat", model:"500", color:"white"}


console.log(car)
console.log(van.type)
console.log(van.model)


//van.doesWork

function test(model) {
    // do nothing
    console.log('testing now')
    if (model == 100){
        console.log('the test worked')
    }
}




// console.timeEnd("whole code")




