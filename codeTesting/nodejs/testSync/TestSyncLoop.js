


/*

Test how asynchronous js is

*/


// this is sync


setTimeout(doSomeCode,1000)

function doSomeCode() {

    console.log('some code is run')
    
}


SomeSize = 1000

for (let i = 0; i < SomeSize; i++) {
    console.log(i)
}

console.log('hello')








