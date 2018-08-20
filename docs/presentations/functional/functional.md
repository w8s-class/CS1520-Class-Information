## Challenge

```javascript
// Write the Following without a For-loop
var data = [1, 2, 3, 4];
for (var i = 0; i < data.length; i++) {
    alert("loopin! " + data[i]);
}
```

Note:
```javascript
function alerter(arr) {
    alert("recursin! " + arr[0]);
    var remaining = arr.slice(1);
    if (remaining.length > 0) {
        alerter(remaining);
    }
}
alerter(data);
```

-###-

## A different way of programming

* Functional programming
* Data stored in the program should be immutable
* Programs should run in a stateless manner

Note:
* immutable:
    * achieved by creating a new value whenever you need to change something
* stateless manner:
    * perform every task as if for the first time, be ignorant of the past

-###-

## Pure Functions

* Building blocks of functional programs
* Should be idempotent
* Operate free from their timing relative to other operations
* Should be free of side-effects

-###-

## Side-Effects to Avoid

* Mutate any shared state or mutable arguments
    * Covered by having immutable data...
* Don't produce any observable output, e.g.,
    * Thrown exceptions
    * Triggered events
    * I/O to devices
    * I/O to display
    * Writes to a log
* Note that this means our programs won't be composed entirely of pure functions

-###-

## Guidelines for functional programming

* Your functions should never rely on outside values
    * Operate only on data passed in as arguments
* All of your functions must accept at least one argument
* All of your functions must return data or another function
* No loops

-###-

## Getting Data from the Server

```javascript
[
    {  "name":      "Crosby",
        "age":      28,
        "points":   [0, 0, 0, 1, 1, 0]
    },
    {   "name":     "Malkin",
        "age":      29,
        "points":   [1, 1, 0, 0, 0, 0]
    },
    {   "name":     "Letang",
        "age":      29,
        "points":   [1, 0, 1, 0, 1]
    }
]
```

Note:
* points against washington is 2016 playoffs,
* letang was out for a game, hence only the five vals

-###-

## Get Player's Average Points Per Game

Note:
* To live code imperative version of playerPoints.js to functional, will need to:
    * create totalAcrossArray func
    * create average func
    * create avgAcrossArray
    * create avgAllSubarrays
    * create grab func
    * create combineArrs func
    * finalize

-###-

## DRYing totalAcrossArray()

* `Array.reduce(callback [, initialValue])`
    * `callback` is a reference to a function that will be called for every item in the array being reduced

-###-

## DRYing totalAcrossArray()

* Will be passed 4 arguments:
    * The value previously returned in the last invocation of the callback, or initialValue, if supplied.
    * The current value of the array being processed
    * The index of the current element being processed
    * The array on which reduce was called
* What should our callback be if we wanted to use reduce() instead of totalAcrossArray()?

Note:
```javascript
function add(a, b) {
    return a + b;
}
```

```javascript
function avgAcrossArray(arr) {
    return average(arr.reduce(add), arr.length);
}
```

* note, that lack of initialValue causes callback to be called fewer (-1) times
    * `[1, 2, 3].reduce(add);` calls:
        * `add(1, 2)`
        * `add(3, 3)`
* `[1, 2, 3].reduce(add, 0);` calls:
    * `add(0, 1)`
    * `add(1, 2)`
    * `add(3, 3)`

-###-

## DRYing avgAllSubarrays()

* `Array.map(callback [, thisArg])`
* `callback` is, again, a reference to a function that will be called for every item in the array being reduced
* However, in this case, the result produced by each call is added into a result array instead of being passed to future calls

-###-

## DRYing avgAllSubarrays()

* Hence, is only passed 3 arguments:
    * Current value
    * Current index
    * Array
* `thisArg` allows you to set what should be referenced by the `this` keyword within `callback`
* What callback could we use to replace `avgAllSubarrays()`?

Note:
```javascript
var avgs = points.map(avgAcrossArray);
```

-###-

## DRYing `grab()`

# How?

Note:
* can define grabName() and grabPoints()
* OR:

```javascript
function grabAtt(att) {
    return function(item) { return item[att]; };
}
var names = data.map(grabAtt("name"));
var points = data.map(grabAtt("points"));
```

-###-

## Another Challenge

* What will this code output?

```javascript
var ex = [];
for (var i = 0; i < 5; i++) {
    ex[i] = function() { document.write(i); };
}
for (var j = 0; j < 5; j++) {
    ex[j]();
}
```

* How can we get it to behave as intended?

-###-

## Closure Example

```javascript
var ex = [];
function funcMaker(i) {
    return function() { document.write(i); };
}
for (var i = 0; i < 5; i++) {
    ex[i] = funcMaker(i);
}
for (var j = 0; j < 5; j++) {
    ex[j]();
}
```

Note:
* A closure
    * The combination of a function and the lexical environment within which that function was declared.
    * non-local variables have been bound either to values or to storage locations (depending on the language)

-###-

## That was a *Brief* Intro to Functional Programming

* For a language designed around functional programming:
    * Haskell

Note:
* More within JavaScript:
    * Underscore.js
