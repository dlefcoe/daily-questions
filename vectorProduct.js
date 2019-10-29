
/*
The code below will change
the heading with id = "myH"
and the paragraph with id = "myP"
in my web page:
*/

var v1 = [5,10, 8]
var v2 = [3, 9, 20]


x = crossProduct(v1, v2)
console.log(x)


x = dotProduct(v1, v2)
console.log(x)


/**
 * @param {array} v1 the first vector.
 * @param {array} v2 the second vector.
 */
function crossProduct(v1, v2) {

    // check same length
    if(v1.length != v2.length){
        return ' v1 is not of same length as v2'
    }

    var s = []

    // build the cross product
    s1 = v1[1]*v2[2] - v1[2]*v2[1]
    s2 =  v1[2]*v2[0] - v1[0]*v2[2]
    s3 = v1[0]*v2[1] - v1[1]*v2[0]

    s.push(s1, s2, s3) 

return s
}


/**
 * performs the dot product process
 * @param {array} v1 the first vector.
 * @param {array} v2 the second vector.
 */
function dotProduct(v1, v2) {

    if(v1.length == v2.length){
        // multiple elements
        var s = 0
        for (let i = 0; i < v1.length; i++) {
            s += v1[i]*v2[i]
        }
    }else{
        return 'v1 is not of same length as v2'
    }
    
return s

}


