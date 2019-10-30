/*

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.


*/




var k = 2
var s = 'waterrfetawx'

s = 'dddaabb'

var letterCount = {a:0,b:0,c:0,d:0,e:0,f:0,g:0,h:0,i:0,j:0,k:0} // ...object of letters of alphabet

palindrome(k,s)



/** 
* check for palindrome
* @param {integer} k number of letters that can be removed 
* @param {string} s the word that is to be checked 
*/
function palindrome(k, s) {
    // some code goes here
    sArray  =s.split('') // string to array

    // every element must occur twice
    
    // count the letter frequency
    sArray.forEach(element => {
        
        if (element in letterCount){
            letterCount[element] += 1
        }else{
            letterCount[element] = 1
        }

    })

    // number of odd occurances
    var odds = 0
    Object.values(letterCount).forEach(element => {
        if (element % 2){
            odds += 1
        }
    })

    // there are too many odd occurances to find a solution
    if (odds > k){
        console.log('cannot resolve with ' + k + ' removals')
        return 'not resolved'
    }else{console.log('this can be resolved !')}
    
    // identify letters to be removed
    Object.entries(letterCount).forEach(([key, val])=>{
        if (val % 2){
            console.log(key + ' needs to be removed')
        }
    })
    // console.log(x)


    // console.log(letterCount)
}



