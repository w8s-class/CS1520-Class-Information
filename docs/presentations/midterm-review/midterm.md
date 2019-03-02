# Overview

* Exam Format
* HTML/CSS
* JavaScript
* Regular Expressions
* HTTP Basics
* Python

-###-

# Exam Format

<!-- .slide: class="section-title" data-background="lib/images/section-bkg.png" -->

-###-

## Exam Sections

* 1 hr 15 min
* 10 Sections
* 1 Bonus Section
* Types
  * Multiple Choice
  * Short Answer
  * Matching
  * Limited Code *(Think fill in the blank, or add a line)*
* Once you are done, you can leave.

-###-

## Approach

* Practical focus
  * I am not concerned if you know RFC numbers or dates of invention, but whether you can combine concepts to solve problems.
* Many of the concepts reviewed may not be directly asked, but play various parts to answer an overall question.

-###-

# HTML/CSS

<!-- .slide: class="section-title" data-background="lib/images/section-bkg.png" -->

-###-

## HTML/CSS Topics

* Understand difference between tags and attributes and how they represent elements
* Common CSS selectors
  * `element`
  * `class`
  * `id`
* How to combine CSS selectors
  * `div.foo#bar`
  * `div p.foo`
  * `div > p`
  * etc.

-###-

# JavaScript

<!-- .slide: class="section-title" data-background="lib/images/section-bkg.png" -->

-###-

## General JavaScript

* How does equality work in JavaScript (a weakly and dynamically typed language)?
  * Coercion, `==` vs `===`
* Math operators with mixed types
  * `+` and `-` with strings and numbers, etc.

-###-

## JavaScript `Arrays` and `Objects`

* How do `Arrays` work in JavaScript?
  * `length`, mixed-types, adding/removing items...
* How can you define and instantiate JavaScript `Objects`?
* How can you extend JavaScript `Objects` after they have been defined?
  * This is especially useful if wanting to extend built-in JavaScript `Objects` or `Objects` defined in libraries.

-###-

## The DOM

* What is the DOM?
* What are different methods JavaScript provides to query the DOM?
  * Think `document.getElementById`...
* How can you manipulate/change the text of an element in the DOM?
* How can you manipulate/change attributes like `class` or `id` in the DOM?

-###-

## Event-Driven Programming

* What are the phases of the JavaScript Event Loop?
* What order will triggered events be fired?
* What are their `targets` vs `currentTargets`?

-###-

## Web Storage

* What is the difference between `localStorage` and `sessionStorage`
* What are the key methods and properties for the JavaScript API?
  * `getItem`, `setItem`, `removeItem`, `clear`, `length`
* What format does the JavaScript API store in web storage?
  * How would you store more complex types like `Arrays` or `Objects`

-###-

# Regular Expressions

<!-- .slide: class="section-title" data-background="lib/images/section-bkg.png" -->

-###-

## Regular Expressions

* I will **not** ask you to *write* regular expressions
* Be comfortable enough with the syntax you can match patterns to the string(s) they will find
* Understand that some symbols mean different things depending on their context
  * e.g. `*` vs `[*]`

-###-

# HTTP Basics

<!-- .slide: class="section-title" data-background="lib/images/section-bkg.png" -->

-###-

## HTTP Methods

* I will **not** ask about OSI Networking Layers
* What are the HTTP Methods?
  * For this course, we generally only care about four of them: `GET`, `POST`, `PUT`, `DELETE`
* What does it mean if a method is `Safe` vs `Unsafe`?
* Which methods are idempotent?

-###-

## HTTP Status Codes

* What are common status codes, status code *ranges*, and what do they mean?
  * `200`?
  * `302`?
  * `404`?
  * `500`?
  * etc.

-###-

# Python

<!-- .slide: class="section-title" data-background="lib/images/section-bkg.png" -->

-###-

## General Python

* What do comments look like?
* What will a slicing pattern do to a string or a list?
  * `list_obj[0:6]`
  * `list_obj[-6:-1]`
  * `list_obj[:4]`
  * `list_obj[1:4:2]`
  * etc.

-###-

## Lists, Dictionaries, and Tuples

* How do you iterate through lists?
* What are the differences between dictionaries and tuples?
* How would you use tuple unpacking?

-###-

## Python Classes

* How do you extend a Python `class`?
* How do you call a parent class function from a child class?
  * When, where, and how do you use the `super()`? When do you not?
* What parent instance properties does a child instance have access to?
* What is the `self` parameter and how do you use it with instance methods?

-###-

## List Comprehensions

* How do you write a list comprehension?
* How do you do a conditional in a list comprehension?

-###-

## Python Decorators

* How is a decorator defined?
* How does a decorator modify the behavior of the function it's decorating?
* What if there is more than one decorator?
  * What order are they executed?
  * When would a decorator modify the arguments vs the return values?

-###-

# Questions

<!-- .slide: class="section-title" data-background="lib/images/section-bkg.png" -->

-###-

## If You Have Questions

1. Slack me for the fastest response
  * Keep questions about course topics in `#general`
  * PM me for questions that *only* pertain to you!
2. Email me and/or Yue.
  * Always `CC` me!
3. Make an appointment for Video Chat