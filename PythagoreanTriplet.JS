/**
 * 
 * 
 * Given an array of integers, determine whether it contains a Pythagorean triplet.
 * Recall that a Pythogorean triplet (a, b, c) is defined by the equation a**2 + b**2= c**2.
 * 
 * 
*/



// we require the combinatorics module: npm i js-combinatorics
const combinatorics = require('js-combinatorics')


let array_of_integers = [1, 2, 3, 4, 5]


let c = combinatorics.combination(array_of_integers, 3)


let isTriplet = pTriplet(array_of_integers)

console.log('contains triplet:', isTriplet)





/**
 * 
 * @param a {array} array of integers
 * 
 * returns true or false
*/
function pTriplet(a) {
    console.log('the array to inspect is:', a)
    //console.log(a)

    // start with a false
    let output = false 

    // get all the combinations of the array
    let cmb = combinatorics.combination(a, 3)

    // loop through the combinations
    cmb.forEach((smallSet)=>{
        // log all the elements
        // console.log(smallSet)

        // square each value
        let aSq = smallSet[0]**2
        let bSq = smallSet[1]**2
        let cSq = smallSet[2]**2

        // check if any satisfy a**2 + b**2= c**2
        if (aSq == bSq + cSq) {
            // message success for this
            console.log(`triplet found: ${aSq}=${bSq}+${cSq}`)
            output = true
        } 
        else if (bSq == aSq + cSq) {
            // message success for this
            console.log(`triplet found: ${bSq}=${aSq}+${cSq}`)
            output = true
        }
        else if (cSq == aSq + bSq) {
            // message success for this
            console.log(`triplet found: ${cSq}=${aSq}+${bSq}`)
            output = true
        }
    })

    // return the result
    return output
}





