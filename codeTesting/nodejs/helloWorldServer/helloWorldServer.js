const http = require('http')

const hostname = '127.0.0.1'
var port = process.env.PORT
port = 8000

console.log('the port is: ' + port)
const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello World!\n')
})

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`)
})



