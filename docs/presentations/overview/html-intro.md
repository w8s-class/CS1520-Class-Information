# HTML



## HTML

* Web documents are commonly formatted and annotated using the HyperText Markup Language
    * First references to HTML made by Sir Tim in 1991
    * First real standard proposed in 1995 with HTML 2.0
    * Current version is HTML5
* HTML documents are built out of HTML elements
    * Elements are delineated by tags



## Intro to HTML5

    <!DOCTYPE html>
    <html>
        <head> </head>
        <body> </body>
    </html>



## HTML Tag Basics

* Most tags are pairs, start and end tags:
    
```
<p> 
  This text would be considered a paragraph
</p>
<em> This text would be emphasized </em>
```

* Comments have their own start and end tags:

```
<!-- This is an HTML comment --> 
<!--
Multiline comment
-->
```



## HTML Tag Basics

* There are also self closing tags
    
```
<br /> <!-- The br tag inputs a line break -->
```



## HTML Tag Basics

* Tags also have attributes
    
```
<a href="http://example.com">click here!</a>
```



## Modern Use of HTML

* HTML is used to present the structure of a document
    * What/where text should be displayed
    * Where images should be placed
* It is often used in conjunction with Cascading Style Sheets (CSS), which describe the presentation of the document
    * Colors, fonts, etc.


### Italics Example

```
<style>
span.italics {font-style: italic;}
</style>
<span class="italics">this will be italicized</span>
```

* Emphasis tag
    
```
<em>this will be italicized</em>
```

* Difference? <!-- .element: class="fragment current-visible" -->

