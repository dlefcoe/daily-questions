http = require("http")
var options = {
  host: 'www.google.com',
  port: 80,
  path: '/index.html'
}

http.get(options, function(res) {
  console.log("Got response COM: " + res.statusCode)
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


