/*

how to get a user input in nodeJS

@dlefcoe
*/


// method 1
const promptSync = require('prompt-sync')()

const name = promptSync('What is your name?')
console.log(`Hey there ${name}`)


let a = 'hello world 1'
let b = 'hello world 2'
let c = 'hello'

console.log(a)
console.log(b)
console.log(c)




// // method 2
// const prm = require('prompt')

// prm.start()
// prm.get(['username', 'email'], function (err, result) {
//     if (err) { console.log('got and error:', err) }
//     console.log('Command-line input received:')
//     console.log('  Username: ' + result.username)
//     console.log('  Email: ' + result.email)

//     console.log('mode code runs here')
//     console.log('mode code runs here')
//     console.log('mode code runs here')
// })




// // method 3 - async
// const readline = require('readline')
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// })

// rl.question('what is your name? ',function (firstName) {
//     console.log(`hey there ${firstName}`)   
    
//     console.log('the rest of the code')
//     console.log('here is more code')
    
//     rl.close() 
// })

// rl.on("close", function() {process.exit(0)})







