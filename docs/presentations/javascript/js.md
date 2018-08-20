# Du-du-duuuuummmm!

<!-- .slide: class="section-title" data-background="/lib/images/section-bkg.png" -->

-###-

# Why?

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="https://media.tenor.com/images/7419e0b27cf1cf57c55516b42b38b2e7/tenor.gif" -->

-###-

## Why?

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="https://media.tenor.com/images/68f3a1332dd5fdb33ed3fe03c7d6c29a/tenor.gif" -->

* By themselves, HTML and CSS can provide a description of the structure and presentation of a document to the browser
	* A static document. <!-- .element: class="fragment" -->

-###-

## But, Why?

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="https://media.tenor.com/images/7593a2834017ecc8fca9919241360f51/tenor.gif" -->

* What are we building in the class?
	* Dynamic applications <!-- .element: class="fragment" -->

-###-

## But, Seriously, Why?!

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="https://media.tenor.com/images/63bb9b7a9edff9624893fcd1a9a6981a/tenor.gif" -->

* Even the most seemingly simple thing can be made annoyingly laborious for users without a dynamic site.
	* Contact Us <!-- .element: class="fragment" -->
	* Signing Up for Git Groups <!-- .element: class="fragment" -->
	* Getting a Slack Invite <!-- .element: class="fragment" -->
	* Shopping Carts <!-- .element: class="fragment" -->
* To do this, we'll need programs that can be fetched from the web and run within the browser <!-- .element: class="fragment" -->

-###-

## Scripting Languages

* Programming languages designed for use within a given runtime environment
	* Often to automate tasks for the user
	* `bash`, `zsh`, `fish`
	* Perl
	* Python
* These languages are often *interpreted*
	* As opposed to *compiled*

-###-

## Compiled vs Interpreted

* Compiled:  before being run, a program is compiled into machine code which is executed by the computer
	* C, C++, C#
* Interpreted:  source code of a program is "executed" directly by an interpreter application
	* Python, Perl, Ruby, PHP

-###-

## Pretty simple, right?

-###-

## Java

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="http://gifimage.net/wp-content/uploads/2017/06/rage-gif-12.gif" -->

* Java source code is compiled into bytecode
	* Which is then run by the JVM
	* so is Java byte code an interpreted language?
* There are implementations for running both Python and Ruby on the JVM (Jython and JRuby)

-###-

## Java

* Both `gcc` and Low Level Virtual Machine (LLVM) compile code in a series of phases:
	* Front-end compilers turn source code into an Intermediate Representation (IR)
	* IR is optimized
	* Optimized IR is turned into machine code
* Tools exist to run LLVM IR on the JVM

Note:

So are all languages interpreted???

* Conclusions:
	* Interpreted vs compiled is more about how languages are used vs how they are built
	* Speed is typically traded off to go with interpreted
	* So why so popular??
		* They're more fun! (as we'll find out...)
* Side note:  why all the focus on the JVM here?
	* It's what you're all used to for one
	* It's been heavily optimized over a number of years, so a great target

-###-

## Scripted vs Interpreted Languages

* Interpreted languages are still compiled to bytecode dynamically, and interpreted in a VM, scripted languages will not need to be compiled.
* This line is very blurred nowadays.
* People use the terms interchangeably.
* [StackOverflow Answer](https://stackoverflow.com/questions/17253545/scripting-language-vs-programming-language)

-###-

## Javascript

* The de facto web client-side scripting language
* Javascript source code can be embedded within or referenced from HTML
	* Through the use of the `<script></script>` tag

Note: Does a script tag mean Javascript? Any language the browser can understand.

-###-

## Javascript Engines

* It is an interpreted language
* Javascript evaluated by the browser in rendering the HTML documents that contain/reference it
* Javascript *engines* are the portion of the browser that interpret Javascript
	* Chrome has V8
	* Firefox has Spidermonkey

-###-

## ECMAScript

"The ECMAScript specification is a standardized specification of a scripting language developed by Brendan Eich of Netscape; initially it was named Mocha, later LiveScript, and finally JavaScript. In December 1995, Sun Microsystems and Netscape announced JavaScript in a press release. In March 1996, Netscape Navigator 2.0 was released, featuring support for JavaScript."

[ECMAScript - Wikipedia](https://en.wikipedia.org/wiki/ECMAScript#ES.Next)


-###-

## ECMAScript 2017

* Added `await`/`async` features
* Previously, ES added classes, modules, iterators, generators, etc.
* Browser support is spotty for ES5 (4 versions old)
* ES5 is more consistent with what we recognize as Javascript.

-###-

## Javascript Variables

* Variable names
	* Are case sensitive
	* Cannot contain keywords
	* Must begin with `$`, `_`, or a letter
		* Followed by any sequence of `$`'s, `_`'s, letters, or digits

Note:
Started as a requirement in languages like FORTRAN or BASIC when:

```fortran
10 V1=100
20 PRINTV1
```
and
```fortran
10V1=100
20PRINTV1
```

So `101V=100` could be `10 1V=100` or `101 V=100` or `1 01V=100`.

Source: [StackOverflow](https://stackoverflow.com/a/5793730)

-###-

## Javascript Numeric Operators

* `+`
* `-`
* `*`
* `/`
* `%`
* `++`
* `--`

-###-

## Javascript Comparison and Boolean Operators

* `==`, `!=`
* `<`, `>`
* `<=`,`>=`
* `&&`, `||`
* `!`
* `&&` and `||` are short circuited

-###-

## Javascript Typing

* Types are tied to values, not variables
* The types of the values stored in a given variable is determined at runtime
	* And can change over the run of the program!
	* This means that checks for type safety are evaluated at run time

-###-

## Implications of dynamic typing in Javascript

* The `+` operator:
	* If one operand is a string value, the other will be coerced into a string and the two strings will be concatenated

-###-

## Implications of dynamic typing in Javascript

* Numeric operators:
	* If one operand is a string value and it can be coerced to a number (e.g., "5"), it will be
	* If string is non-numeric, result is `NaN` (`NotaNumber`)
	* We can also explicitly convert the string to a number using parseInt and parseFloat

-###-

## Implications of dynamic typing in Javascript

* [Comparisons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators):
	* `==` and `!=` allow for type coercion
	* What does this mean?

Note: Do we throw typing errors all over the place? No! We try to resolve type issues (avoid type safety)

-###-

## Comparing both type and value

* An additional equality operator and inequality operators are defined to help deal with odd behavior presented by `==` and `!=`:
	* `===` returns true only if the variables have the same value and are of the same type
		* If type coercion is necessary to compare, returns false
	* `!==` returns true if the operands differ in value or in type

Note:
* js1
* js2
* js3

-###-

## Javascript Functions

* `function foo(param1, param2, param3) { ... } `
* Return types are not specified
* Param types are not specified

-###-

## Javascript Functions

* Functions execute when they are called, just as in any language
	* Because of this, function definitions should be in the head HTML element
```html
<head>
	<script>function foo(param) {...} </script>
</head>
```

-###-

## Javascript Functions

* Parameters are all passed by value
* No parameter type-checking

-###-

## Javascript Functions

* Numbers of formal and actual parameters do not have to correspond
* Extra actual parameters are ignored
* Extra formal parameters are undefined
* All actual parameters can be accessed regardless of formal parameters by using the arguments array

Note: js4

-###-

## Javascript Arrays

* More relaxed compared to Java arrays
	* Size can be changed and data can be mixed
	* Cannot use arbitrary keys
		* Similar to a hashmap

-###-

## Javascript Arrays

* Multiple ways to create arrays:

```javascript
// Using the new operator and a constructor with multiple arguments:
var A = new Array("hello", 2, "you");
```
```javascript
// Using the new operator and a constructor with a
//    single numeric argument
var B = new Array(50);
```
```javascript
// Using square brackets to make a literal
var C = ["we", "can", 50, "mix", 3.5, "types"];
```

-###-

## Javascript Array Length

* Like in Java, length is an attribute of all array objects
	* *Unlike Java, this attribute is mutable*
* In Javascript it does not necessarily represent the number of items or even memory locations in the array
* Actual memory allocation is dynamic and occurs when necessary
* An array with length = 1000 may in fact only have memory allocated for 5 elements
* When accessed, empty elements are `undefined`

-###-

## Javascript Array Methods

* `concat`
	* Concatenate two arrays into one
* `join`
	* Combine array items into a single string (commas between)
* `push`, `pop`, `shift`, `unshift`
	* `push` and `pop` are a "right stack" (to/from end)
	* `shift` and `unshift` are a "left stack" (to/from beginning)

-###-

## Javascript Array Methods

* <span class="fragment highlight-red">`sort`</span>
	* Sort by default compares using alphabetical order
	* To sort numerically, we pass in a comparison function defining how the numbers will be compared
* <span class="fragment highlight-red">`reverse`</span>
	* Reverse the items in an array

Note: js5

-###-

## Sorting comparison function psuedocode

```javascript
function compare(a, b) {
	if (a is less than b by some ordering criterion) {
		return -1;
	}

	if (a is greater than b by the ordering criterion) {
		return 1;
	}

	// a must be equal to b
	return 0;
}
```

-###-

## Javascript is an object-based language

* <span class="fragment highlight-red">**NOT** object-oriented</span>
* It has and uses objects, but does not support some features necessary for object-oriented languages
* E.g., Class inheritance and polymorphism are not supported (As far as we are concerned)

-###-

## Javascript Objects

* Javascript objects are represented as property-value pairs
	* In some ways similar to hashmaps
		* The object is analogous to the array backing the hashmap, and the properties are analogous to the keys

-###-

## Javascript Objects

* Property values can be data or functions (methods):

```javascript
var my_tv = new Object();
my_tv.brand = "Samsung";
my_tv.size = 46;
my_tv.jacks = new Object();
my_tv.jacks.input = 5;
my_tv.jacks.output = 2;
```

-###-

## Object Details

* Note that the objects can be created and their properties can be changed dynamically
* Objects all have the same type: Object
* Constructor functions for objects can be written, but these do not create new data types,  just easy ways of uniformly initializing objects

-###-

## Object Details

```javascript
function TV(brand, size, injacks, outjacks) {
	this.brand = brand;
	this.size = size;
	this.jacks = new Object();
	this.jacks.input = injacks;
	this.jacks.output = outjacks;
}
//...
var my_tv = new TV("Samsung", 46, 5, 2);
```

Note:

* js6
* js7
