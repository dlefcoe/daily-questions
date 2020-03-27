/*

You are given an string representing the initial conditions of some dominoes.
Each element can take one of three values:


L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.

Determine the orientation of each tile when the dominoes stop falling.
Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.
Given the string ..R...L.L, you should return ..RR.LLLL.


@dlefcoe

question: what happens if the domino is this RL
do they fall on each other ?


*/



// code to run
dominoDrop()





function dominoDrop() {
    console.log('the main function ran')
    
    var s = '.L.R....L'
    var sArray = s.split('') // split into array
    
    // log the result    
    console.log('the start array: ' + sArray)

    /*
    the number of runs required depends on the length of the '.'
    lets call this the loopLength
    */

    //console.log('the length is ' + sArray.length)
   
    // initialise loopLength
    var loopLength = 0
    var loopLenMax = 0
    for (let i = 0; i < sArray.length; i++) {
        if (sArray[i]=='.') {
            loopLength += 1
            if (loopLength > loopLenMax) {
                loopLenMax = loopLength    
            }
        } else {
            loopLength = 0
        }
    }

    console.log('consecutive dots: ' + loopLenMax)

    // inspect left most item
    if (sArray[0] == '.') {
        // need to inspect the next item
        if (sArray[1]=='L') {
            // drops to the left
            sArray[0] = 'L'
        }
    } else {
        // unchanged
    }

    
    // inspect the middle items in the list
    for (let i = 1; i < sArray.length-2; i++) {
        
        
        if (sArray[i]=='.') {
            // has no direction

            // check the left
            if (sArray[i-1]=='L') {
                leftDom = -1
            } else if(sArray[i-1]=='.') {
                leftDom = 0
            } else if(sArray[i-1] == 'R'){
                leftDom = +1
            }
            
            // check the right
            if (sArray[i+1]=='L') {
                rightDom = -1
            } else if(sArray[i+1]=='.') {
                rightDom = 0
            } else if(sArray[i+1] == 'R'){
                rightDom = +1
            }

            // add the values
            netForce = leftDom + rightDom

            // the net force determines the direction
            if (netForce == -1) {
                sArray[i] = 'L'
            } else if (netForce == 1){
                sArray[i] = 'R'
            } else { 
                // nothing happens
            }

        }

    }


    // inspect right most item
    if (sArray[sArray.length-1] == '.') {
        // need to inspect the next item
        if (sArray[sArray.length-2]=='R') {
            // drops to the left
            sArray[sArray.length-1] = 'R'
        }
    } else {
        // unchanged
    }

    console.log('the final result: ' + sArray)
}


/**
 * in order to complete this properly, the program needs to create a new array to be populated 
 *  this will be an experiment to be left to the reader for now....
 */



 



/**
 * random code to test
 * @param {array} v1 the first vector.
 * @param {array} v2 the second vector.
 */
function testCode() {
    // run through each to check
    sArray.forEach(element => {
        console.log(element)
    })
    
}


