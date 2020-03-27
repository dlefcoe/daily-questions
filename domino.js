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
    var rArray = []
    
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
            rArray[0] = 'L'
        }
    } else {
        // unchanged
        rArray[0] = sArray[0]
    }

    
    // inspect the middle items in the list
    for (let i = 1; i <= sArray.length-2; i++) {
        
        
        if (sArray[i]=='.') {
            // has no direction

            // nothing happens in these cases
            // left + right
            // right + left
            // . + .
            // . + right
            // left + .
            rArray[i] = sArray[i]

            // cases when there is pushing and rArray changes

            // left + left
            if ((sArray[i-1]=='L') && (sArray[i+1]=='L')) {
                rArray[i] = 'L'
            }

            // right + right
            if ((sArray[i-1]=='R') && (sArray[i+1]=='R')) {
                rArray[i] = 'R'
            }

            // . + left
            if ((sArray[i-1]=='.') && (sArray[i+1]=='L')) {
                rArray[i] = 'L'
            }


            // right + .
            if ((sArray[i-1]=='R') && (sArray[i+1]=='.')) {
                rArray[i] = 'R'
            }





        } else {
            // the direction is known
            rArray[i] = sArray[i]
        }

    }


    // inspect right most item
    if (sArray[sArray.length-1] == '.') {
        // need to inspect the next item
        if (sArray[sArray.length-2]=='R') {
            // drops to the right
            rArray[sArray.length-1] = 'R'
        }
    } else {
        // unchanged
        rArray[sArray.length-1] = sArray[sArray.length-1]
    }

    console.log('the final result: ' + rArray)
}








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


