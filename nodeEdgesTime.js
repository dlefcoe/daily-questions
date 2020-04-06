/*

A network consists of nodes labeled 0 to N.
You are given a list of edges (a, b, t), describing the time t it takes for a message to be sent from node a to node b.
Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.


*/


// first thing to note is that js does not handle Tuples like py.
// so need to conert to arrays.



edges = [
    [0, 1, 5],
    [0, 2, 3],
    [0, 5, 4],
    [1, 3, 8],
    [2, 3, 1],
    [3, 5, 10],
    [3, 4, 5]
]


// isJoin(5, [3,4,2,6,4,5,9])
// isJoin(5, [3,4,2,6,4,8,9])

nodeEdgesTime(edges)

function nodeEdgesTime(edges) {
    // for(i in edges){
    //     console.log(edges[i])
    // }

    // pre loop initialise
    var jumpVector = []
    for (j of edges) {
        console.log(j)

        // possible jumps

        
        // identify each array that starts with 0
        if(j[0]==0) {
            jumpVector.push(j[1])
        }
    
    }
    console.log('the jump vector options: ')
    console.log(jumpVector)

    // now inspect the jumps
    for (j of edges){
        for (v of jumpVector) {
            if (j[0]==v){
                console.log('true', j[0], v)
            } else {
                //console.log('false', j[0], v)
            }
        } 
        

    }

    
    
    // edges.forEach(element => {
    //     console.log(element)
        
    // })


    // steps to take

    // not sure the question makes sense.

}



/**
 * 
 * @param {number} n, number to look up 
 * @param {number[]} v, the lookup vector of numbers
 * 
 * @returns {boolean} if included=True, otherwise=False
 */
function isJoin(n, v) {

    console.log('this is v: ')
    console.log(v)

    // check if value n is in the array v    
    var result = v.includes(n)
    console.log(result)

    return result

}




