# functions in JS
How to use functions in JS and NodeJS


### contents
1. JavaScript Functions
2. JavaScript Function Syntax
3. Function Invocation
4. Function Return
5. Why Functions?
6. The () Operator Invokes the Function
7. Functions Used as Variable Values
8. Local Variables




## JavaScript Functions
A JavaScript function is a block of code designed to perform a particular task.
A JavaScript function is executed when "something" invokes it (calls it).


> example
```javascript

function myFunction(p1, p2) {
  return p1 * p2;   // The function returns the product of p1 and p2
}

```


## JavaScript Function Syntax
A JavaScript function is defined with the `function` keyword, followed by a **name**, followed by parentheses **()**.

The parentheses may include parameter names separated by commas:
**(parameter1, parameter2, ...)**

The code to be executed, by the function, is placed inside curly brackets: **{}**

>example
```javascript

function name(parameter1, parameter2, parameter3) {
  // code to be executed
}

```

Function **parameters** are listed inside the parentheses () in the function definition.
Function **arguments** are the **values** received by the function when it is invoked.
Inside the function, the arguments (the parameters) behave as local variables.

> A Function is much the same as a Procedure or a Subroutine, in other programming languages.



## Function Invocation
The code inside the function will execute when "something" **invokes** (calls) the function:

* When an event occurs (when a user clicks a button)
* When it is invoked (called) from JavaScript code
* Automatically (self invoked)
* if it calls itself (recursive functions)


We will learn a lot more about function invocation later in this tutorial



## Function Return

When JavaScript reaches a `return` statement, the function will stop executing.
If the function was invoked from a statement, JavaScript will "return" to execute the code after the invoking statement.
The program returns on the next line of code.


> example
Calculate the product of two numbers, and return the result:

```javascript

var x = myFunction(4, 3);   // Function is called, return value will end up in x

function myFunction(a, b) {
  return a * b;             // Function returns the product of a and b
}

```


## Why Functions?
You can reuse code: Define the code once, and use it many times.
You can use the same code many times with different arguments, to produce different results.

> example
Convert Fahrenheit to Celsius:

```javascript

function toCelsius(fahrenheit) {
  return (5/9) * (fahrenheit-32);
}

console.log(toCelsius(50))
console.log(toCelsius(75))
console.log(toCelsius(100))

```



## The () Operator Invokes the Function
Using the example above, `toCelsius` refers to the function object, and `toCelsius()` refers to the function result.

```javascript

function toCelsius(fahrenheit) {
  return (5/9) * (fahrenheit-32);
}

console.log(toCelsius(50))   // get the result
console.log(toCelsius)       // get the object :  function toCelsius(f) { return (5/9) * (f-32); }

```


## Functions Used as Variable Values
Functions can be used the same way as you use variables, in all types of formulas, assignments, and calculations.

> example
Instead of using a variable to store the return value of a function:

```javascript
var x = toCelsius(77);
var text_using_variable = "The temperature is " + x + " Celsius";

var text_using_function = "The temperature is " + toCelsius(77) + " Celsius";

console.log(text_using_variable)
console.log(text_using_function)

```


## Local Variables
Variables declared within a JavaScript function, become **LOCAL** to the function.
Local variables can only be accessed from within the function.

> example

```javascript

// code here can NOT use carName

function myFunction() {
  var carName = "Volvo";
  // code here CAN use carName
  console.log(carName)
}

// code here can NOT use carName

```

Since local variables are only recognized inside their functions, variables with the same name can be used in different functions.
Local variables are created when a function starts, and deleted when the function is completed.




the end.
-------


