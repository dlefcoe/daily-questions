/*

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


*/


// itertools is not a natural option in node.js

// do this as a binomial tree method
/*
        0
   2          3
1       0          1
    5       0           1
        3         4 
            1
*/


rnd = Math.round(Math.random()*10)
console.log('random number')
console.log(rnd)

m = [
    [0,3,1,1],
    [2,0,0,4],
    [1,5,3,1]
    ]


// generate a random matrix to test
m = generateRandomMatrix(3,3)

m = [
    [7,1,4,9],
    [1,9,1,4],
    [4,1,9,1],
    [1,9,1,4]
]

console.log(m)

// test matrix
console.log('---some tests---')
console.log(m[0][0])
console.log(m[0][1])

d = 0
r = 1
console.log(m[d][r])
console.log('---end tests---')



rMax = m[0].length-1 // max width
dMax = m.length-1 // max height
console.log('matrix width:', rMax)
console.log('matrix height:', dMax)

var highestPath = {value:0, path: ''}

// iterate through all possible combinations
const root = m[0][0]

console.log('--- matrix walk through ---')
walkThroughMatrix(0,0,0,'start:')
console.log(highestPath)

/**
 * walk through matrix recursively
 * @param {number} n, the starting point (the first call should be n=0)
 * @param {number} r , the position to the right
 * @param {number} d , the position down
 * @param {string} path, string of the moves
 */
function walkThroughMatrix(n, r, d, path) {
    var v = n + m[d][r]
    var path = path + '-> [' + d + ',' + r + '] '
    // can we go right
    if (r < rMax){
        // take a right step
        walkThroughMatrix(v, r+1, d, path)
    }else{
        // reached the far right
            // can we go down
            if (d < dMax){
                // take a down step
                walkThroughMatrix(v, r, d+1, path)
            }else{
                // reached the end
                // console.log(v, path)
                if (v>highestPath.value){
                    highestPath.value = v
                    highestPath.path = path
                }
                return 'done'
            }

    }

    // can we go down
    if (d < dMax){
        // take a down step
        walkThroughMatrix(v, r, d+1, path)
    }else{
        // reached the bottom
            // can we go right
            if (r < rMax){
                // take a right step
                walkThroughMatrix(v, r+1, d, path)
            }else{
                // reached the end
                // console.log(v, path)
                if (v>highestPath.value){
                    highestPath.value = v
                    highestPath.path = path
                }
                return 'done'
            }
    }



}



/**
 * generate a random matrix
 * @param {number} n the height of the matrix
 * @param {number} m the width of the matrix
 */
function generateRandomMatrix(n, m) {
    mtrx = []
    for (let i = 0; i < n; i++) {
        mtrx.push([])
        for (let j = 0; j < m; j++) {
            mtrx[i].push(Math.round(Math.random()*10))
        }
    }
    return mtrx
}

