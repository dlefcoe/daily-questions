/*
This problem was asked by Spotify.

Write a function, throw_dice(N, faces, total), 
that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.


*/

var mathjs = require('mathjs')
var itt = require('itertools')
var fs = require('fs')


/**
 * 
 * @param {number} N number of dice
 * @param {number} faces number of faces on dice 
 * @param {number} total specific total that user wants 
 * 
 * @returns {number} number of possible ways
 */
function diceRoll(N, faces, total){

    // check that total is high enough
    if (total < N) { 
        console.log(`the total of ${total} is too low given ${N} dice`)
        return 0
    }

    // check the total is not too high
    if (total > faces * N){
        console.log(`the total of ${total} is too high given ${N} dice and ${faces} faces`)
        return 0
    }

    // work out all sums
    perm = mathjs.permutations(3,2)
    comb = mathjs.combinations(3,2)
    console.log(`permutations: ${perm}`)
    console.log(`combinations: ${comb}`)

    possibleOutcomes = faces**N
    console.log(`there are ${possibleOutcomes} possible outcomes`)

    // brute force iteration

    /** 
     * looks like this
     * 
     * for i = 1; i <= N
     * (for f = 1; f <= faces),  (for f = 1; f <= faces), (for f = 1; f <= faces)
     * 111
     * 112
     * 113
     * 114
     * 115
     * 116
     * 
     * 121
     * 122
     * 123
     * 
     * 
     * */ 
    

    // pre loop initialise
    var diceArray = []
    // fill with n dice
    for(i = 1; i<=N; i++) diceArray.push(faces) 

    

    console.log(diceArray)


    //console.log(diceArray)
    var combsArray = []
    var miniArray = []
    for(i=1;i<=N;i++){
        miniArray.push(1)
    }
    console.log('The mini array size', miniArray)

    
    // need to improve this to be general.
    for(d=1;d<=faces;d++){
        for(e=1;e<=faces;e++){
            for(f=1;f<=faces;f++){
                    miniArray = [d,e,f]
                    combsArray.push(miniArray)
            }
        }
    }

    /**
     * function inside a function
     * @param {*} val 
     */
    function funInfun(val) {
        console.log(val)
    }

    funInfun("embedded function to run")


    countTotals = 0
    console.log('the sums: ')
    combsArray.forEach((e)=>{
        s = mathjs.sum(e)
        if(s == total){
            console.log(`${s} from ${e}`)
            countTotals++
        }

    })
    console.log('the number of matching items:', countTotals)


    // run permutations function
    perm = getPermutations([1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6],3)
    perm = getPermutations([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6],3)

    //z = getPermutations([1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],3)

    console.log('permutation function results: ')
    // console.log(z)

    var date = new Date()
    console.log(`this is the date: ${date}`)
    fileName = `permsFile${date.getHours()}${date.getMinutes()}${date.getSeconds()}.txt`


    perm.forEach((x)=>{
        // write file
        fs.appendFile(fileName, x + '\n', function (err) {
            if (err) throw err;
            // console.log('saved!');
        })
        
        //console.log(x)
    })
    console.log('files should be saved here:', fileName)




    //combsArray = itt.permutations([1,2,3,4,5,6])

    //combsArray = k_combinations([1,2,3,4,5,6],3)
    //combsArray = combinations([1,2,3,4,5,6])

    // var miniArray = []
    // for(f=1;f<=faces;f++){
    //     for(i=1;i<=N;i++){
    //         miniArray = [1,1,f]
    //     }
    //     combsArray.push(miniArray)

    // }

    /**
     * 111
     * 112
     * 113
     * 114
     * 115
     * 116
     * 121
     * 122
     * 123
     * 124
     * 125
     * 126
     * 131
     * 131
     * 133
     * 134
     * 135
     * 136
     * 
     */

    
    



    // for(i=1;i<=N;i++){
    //     var miniArray = []
    //     for(f=1; f<=faces; f++){
    //         miniArray.push(f)
    //         for(f=1; f<=faces; f++){
    //             miniArray.push(f)
    //             for(f=1; f<=faces; f++){
    //                 miniArray.push(f)
    //                 combsArray.push(miniArray)
                    
    //             }
    //         }
    //     }
        
    // }

    // for (f=1; f <= faces; f++){
    //     //var miniArray = []
    //     for (i = 1; i <= N; i++) {
    //         miniArray.push(f)
    //     }
    //     combsArray.push(miniArray)
    // }


    console.log('the combinations array:')
    if(combsArray.length > 10){
        console.log('array > len 10')
    } else {
        console.log(combsArray)
    }

}





/**
 * function to populate mini array
 * might be recursive
 * 
 * 
 */
function populateMiniArray(faces){

    for(f=1;f<=faces;f++){
        miniArray = [d,e,f]
    }
    a = []

    return a

}







/**
 * this is an externally copoed function
 * @param {array}  
 * @param {number} size 
 */

function getPermutations(array, size) {

    function p(t, i) {
        if (t.length === size) {
            result.push(t);
            return;
        }
        if (i + 1 > array.length) {
            return;
        }
        p(t.concat(array[i]), i + 1);
        p(t, i + 1);
    }

    var result = [];
    p([], 0);
    return result;
}

// var array = ['a', 'b', 'c', 'd'];
// array = [1,2,3,4,5,6]
// console.log(getPermutations(array, 3));



diceRoll(3, 6, 7)  // working example
diceRoll(3, 6, 2)  // failed example




function k_combinations(set, k) {
	var i, j, combs, head, tailcombs;
	
	// There is no way to take e.g. sets of 5 elements from
	// a set of 4.
	if (k > set.length || k <= 0) {
		return [];
	}
	
	// K-sized set has only one K-sized subset.
	if (k == set.length) {
		return [set];
	}
	
	// There is N 1-sized subsets in a N-sized set.
	if (k == 1) {
		combs = [];
		for (i = 0; i < set.length; i++) {
			combs.push([set[i]]);
		}
		return combs;
	}
	
	// Assert {1 < k < set.length}
	
	// Algorithm description:
	// To get k-combinations of a set, we want to join each element
	// with all (k-1)-combinations of the other elements. The set of
	// these k-sized sets would be the desired result. However, as we
	// represent sets with lists, we need to take duplicates into
	// account. To avoid producing duplicates and also unnecessary
	// computing, we use the following approach: each element i
	// divides the list into three: the preceding elements, the
	// current element i, and the subsequent elements. For the first
	// element, the list of preceding elements is empty. For element i,
	// we compute the (k-1)-computations of the subsequent elements,
	// join each with the element i, and store the joined to the set of
	// computed k-combinations. We do not need to take the preceding
	// elements into account, because they have already been the i:th
	// element so they are already computed and stored. When the length
	// of the subsequent list drops below (k-1), we cannot find any
	// (k-1)-combs, hence the upper limit for the iteration:
	combs = [];
	for (i = 0; i < set.length - k + 1; i++) {
		// head is a list that includes only our current element.
		head = set.slice(i, i + 1);
		// We take smaller combinations from the subsequent elements
		tailcombs = k_combinations(set.slice(i + 1), k - 1);
		// For each (k-1)-combination we join it with the current
		// and store it to the set of k-combinations.
		for (j = 0; j < tailcombs.length; j++) {
			combs.push(head.concat(tailcombs[j]));
		}
	}
	return combs;
}


/**
 * Combinations
 * 
 * Get all possible combinations of elements in a set.
 * 
 * Usage:
 *   combinations(set)
 * 
 * Examples:
 * 
 *   combinations([1, 2, 3])
 *   -> [[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
 * 
 *   combinations([1])
 *   -> [[1]]
 */
function combinations(set) {
	var k, i, combs, k_combs;
	combs = [];
	
	// Calculate all non-empty k-combinations
	for (k = 1; k <= set.length; k++) {
		k_combs = k_combinations(set, k);
		for (i = 0; i < k_combs.length; i++) {
			combs.push(k_combs[i]);
		}
	}
	return combs;
}