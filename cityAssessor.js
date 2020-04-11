/*

I changed this question to look at the local tallest buildings.


You are given an array representing the heights of neighboring buildings on a city street, from east to west.
The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun,
in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3,
since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?

*/


// globals
let buildings = [3, 7, 8, 3, 6, 1]
let goodView = 0




// the first building
if (buildings[0]>buildings[1]) {goodView++}

// the middle buildings
cityAssessor(buildings)

// the last building
if (buildings[buildings.length-1]>buildings[buildings.length-2]) {goodView++}

console.log(goodView)




/**
 * 
 * @param {array} buildings the array of buildings heights
 */
function cityAssessor(buildings) {
    // check array size
    if (buildings.length <= 2) return 0

    for (let i = 1; i < buildings.length - 2; i++) {
        if(buildings[i]>buildings[i-1] && buildings[i]>buildings[i+1]){
            goodView++
        }
    }
    
}



/**
 * 
 * @param {array} buildings array of buildings
 * 
 * @returns {integer} number of buildings that can see the sun setting
 */
function westLooker(buildings) {

    // the most westerly bulding can always see the sun set
    let canSee = 1
    
    // the initial height
    let heightMax = buildings[buildings.length-1]
    

    // go through the array backwards
    for (let i = buildings.length-2; i >= 0; i--) {
        if(buildings[i] > heightMax){
            canSee++
            heightMax = buildings[i]
        }
    }

    return canSee
}

console.log('good views:',westLooker(buildings))