const https = require('https') // https://nodejs.dev/making-http-requests-with-nodejs

// the url constructor
var url = 'https://www.ishares.com'
var urlListPrefix = '/uk/individual/en/products/'
var isf = '251795'
var urlListSuffix = '/?switchLocale=y&siteEntryPassthrough=true'

var options = {
    hostname: url,
    path: urlListPrefix + isf + urlListSuffix,
    method: 'GET'
    }

// just check for the bbc website
var options = {
    hostname: 'www.bbc.co.uk',
    path: '/',
    method: 'GET'
    }


// just check for the ishares website
var options = {
    hostname: 'www.ishares.com/uk/individual/en/products/251795/?switchLocale=y&siteEntryPassthrough=true',
    path: '/',
    method: 'GET',
    //port: 8080
    }


const req = https.request(options, res => {
    console.log(`statusCode: ${res.statusCode}`)

    res.on('data', d => {
        process.stdout.write(d)
        })
    })

req.on('error', error => {
    console.error(error)
    })

req.end()


/*

x = http.get(url,(res, msg)=>{})

url = 'www.bbc.co.uk'

getWebData(url)

function getWebData(url){
    //var xhttp = new XMLHttpRequest()
    var xhttp = new xmlhttprequest()
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        // Typical action to be performed when the document is ready:
        
        console.log(xhttp.responseText)
        // var response = JSON.parse(xhttp.responseText)

        console.log('inside the if statement')
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}


*/

