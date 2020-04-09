/**
 * 
 * 
 *  functions in JS
 * 
 * 
 * 
*/


let result = myFunction(5,10)
console.log(result)

productAndSum(1, 2, 3)  // expecting 2*3 = 6,  6+1 = 7

function myFunction(p1, p2) {
    return p1 * p2;   // The function returns the product of p1 and p2
    }



function productAndSum(value1, value2, value3) {
    // code to go inside the function
    console.log('the product of value2 and value3, summed to value1 :')
    console.log(value1 + value2 * value3)
}
  

function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
  }
  
  console.log('function with () used:')
  console.log(toCelsius(50))   // get the result
  
  console.log('function with no brackets used:')
  console.log(toCelsius)       // get the object :  function toCelsius(f) { return (5/9) * (f-32); }

  
  console.log('Testing using variable compared to using function')
  var x = toCelsius(77);
  var text_using_variable = "The temperature is " + x + " Celsius";
  
  var text_using_function = "The temperature is " + toCelsius(77) + " Celsius";
  
  console.log(text_using_variable)
  console.log(text_using_function)
  


  function aboutCar() {
    var carName = "Volvo";
    // code here CAN use carName
    console.log(carName)
  }
  

aboutCar()





