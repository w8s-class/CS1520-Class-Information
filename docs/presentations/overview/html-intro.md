# HTML

-###-

## HTML

* Web documents are commonly formatted and annotated using the HyperText Markup Language
    * First references to HTML made by Sir Tim in 1991
    * First real standard proposed in 1995 with HTML 2.0
    * Current version is HTML5
* HTML documents are built out of HTML elements
    * Elements are delineated by tags

-###-

## Intro to HTML5

    <!DOCTYPE html>
    <html>
        <head> </head>
        <body> </body>
    </html>

-###-

## HTML Tag Basics

* Most tags are pairs, start and end tags:
    
```html
<p> 
  This text would be considered a paragraph
</p>
<em> This text would be emphasized </em>
```

* Comments have their own start and end tags:

```html
<!-- This is an HTML comment --> 
<!--
Multiline comment
-->
```

-###-

## HTML Tag Basics

* There are also self closing tags
    
```html
<br /> <!-- The br tag inputs a line break -->
```

-###-

## HTML Tag Basics

* Tags also have attributes
    
```html
<a href="http://example.com">click here!</a>
```

-###-

## Modern Use of HTML

* HTML is used to present the structure of a document
    * What text should be displayed
    * The hierarchical structure of the information
    * Where images should be placed in context of content

-###-

## HTML and CSS

* It is often used in conjunction with Cascading Style Sheets (CSS), which describe the presentation of the document
    * Colors, fonts, etc.
    * Layout of content

-###-

### Italics Example

```html
<style>
span.italics {font-style: italic;}
</style>
<span class="italics">this will be italicized</span>
```

* Emphasis tag
    
```html
<em>this will be italicized</em>
```

* Difference? <!-- .element: class="fragment current-visible" -->

-###-

## The `id` Attribute

* `id` allows you target a specific instance of an element with CSS and JavaScript.

```html
<!-- IDs should be unique on a page-->
<span id="unique"></span>
<span id="wrong"></span>
<span id="wrong"></span>
```

-###-

## The `class` Attribute

* `class` allows you target a group of elements with CSS and JavaScript.

```html
<!-- IDs should be unique on a page-->
<!-- Classes can repeat and be applied to different elements-->
<span id="unique" class="custom"></span>
<span id="wrong" class="custom"></span>
<span id="wrong" class="custom"></span>
<div class="custom"></div> 
```

-###-

## Targeting Selectors with CSS

```html
<span id="unique" class="custom">Test</span> 
```

```css
span { /* CSS selectors with no period or octothorpe are targeting html elements */
    color: red;
}

#unique { /* CSS selector beginning with an octothorpe target IDs */
    color: blue;
}

.custom { /* CSS selector beginning with a period target classes */
    color: green;
}
```

Note:
* You can combine selectors `span.custom {}` to only apply styles to element `span` with class `custom`

-###-

# Assignment

-###-

## Assignment 1

* Create github user
* Join Slack chat
    * I will post the invite link to CourseWeb
    * Message me **on Slack** with any information that is important to interact with you
        * Preferred pronouns, preferred name, etc.
        * Special accommodations in accordance with university policy
        * your github username
* Join github class group
