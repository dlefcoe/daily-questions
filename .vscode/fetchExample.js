print = console.log // use print instead of console.log



http = require("http")
var options = {
    host: 'www.google.com',
    //port: 80,
    path: '/index.html'
}



http.get(options, function(res) {
    console.log("Got response COM: " + res.statusCode)
    print('hello world')

    let output = ''
    let i = 0

    res.on('data', function(chunk) {
        output += chunk
        i += 1
        console.log('found chunk of data... ' + i)})

    res.on('end',function(){
        console.log('some output: \n ', output)}) 

    

}).on('error', function(e) {
  console.log("Got error: " + e.message)
})


var options = {
  host: 'www.google.com.au',
  port: 80,
  path: '/index.html'
}

http.get(options, function(res) {
  console.log("Got response AU: " + res.statusCode)
}).on('error', function(e) {
  console.log("Got error: " + e.message)
})


