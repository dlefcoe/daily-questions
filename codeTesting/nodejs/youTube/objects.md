# javascript objects


in real life a car is an **object**

A car has **properties** like weight and color, and **methods** like start and stop:


|**properties**  | **methods**  |
|----------------|--------------|
|  car.name      | car.start()  |
|  car.model     | car.drive()  |
|  car.weight    | car.brake()  |
|  car.colour    | car.stop()   |



All cars have the same **properties**, but the property **values** differ from car to car.
All cars have the same **methods**, but the methods are performed **at different times**.


## JavaScript Objects

This code assigns a **simple value** (Fiat) to a **variable** named car:

``` javascript
var car = "Fiat";
```

This code assigns **many values** (Fiat, 500, white) to a **variable** named car:

``` javascript
var car = {type:"Fiat", model:"500", color:"white"};
```


The values are written as **name:value** pairs (name and value separated by a colon).


## Object Definition
You define (and create) a JavaScript object with an object literal:

``` javascript
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
```

Spaces and line breaks are not important. An object definition can span multiple lines:

``` javascript
var person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};

```



## Object Properties
The **name:values** pairs in JavaScript objects are called **properties**:

**Property** |	**Property Value**
----------------------------------
firstName    |	John
lastName     |	Doe
age	         |  50
eyeColor	 |  blue


## Accessing Object Properties
You can access object properties in two ways:

`objectName.propertyName`
or
`objectName["propertyName"]`


example 1.
`person.lastName;`

example 2.
`person["lastName"];`


## Object Methods
Objects can also have methods.

**Property** |	**Property Value**
----------------------------------
firstName    |	John
lastName     |	Doe
Accessing    |	50
eyeColor	 |  blue
fullName	 |  `function() {return this.firstName + " " + this.lastName;}`



A method is a function stored as a property.

> example

``` javascript

var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};

```


## The _this_ Keyword
In a function definition, `this` refers to the "owner" of the function.
In the example above, `this` is the **person object** that "owns" the `fullName` function.
In other words, `this.firstName` means the `firstName` property of **this object**.


## Accessing Object Methods
You access an object method with the following syntax:

> `objectName.methodName()`

example
> `name = person.fullName();`

If you access a method **without** the () parentheses, it will return the **function definition**:

example
> `name = person.fullName;`




