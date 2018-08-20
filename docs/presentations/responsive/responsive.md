## Make it work, but small...

* You've built your RESTful API, and have it running with a server-side app
* Will allow you to not only support JS app easily, but also mobile apps
* Now you just have to write the native mobile app...

-###-

## But wait!

What about just serving the JS app to mobile?

-###-

## Viewports

![Viewports](https://i.stack.imgur.com/KaRaG.png)

Note:
* Note, this is mobile browser dev approach to solve this problem
    * layout viewport is always the same, just change portion of it being displayed
* How can you, as the web app dev solve it better?

-###-

## Responsive Design

> If you put water into a cup, it becomes the cup. You put water into a bottle and it becomes the bottle. You put it in a teapot, it becomes the teapot.

>  -- Bruce Lee

Note:
* demo <https://culturaldistrict.org/> as example of what would be great responsive design

-###-

## When a pixel is not a pixel...

* What happens when the user zooms in on their phone?
    * Need to display same portion of the page using more pixels
    * Should this scale up the size of the layout viewport?
* Pixel density of displays has begun to increase dramatically
    * How can we render the same page on both standard and HiDPI displays?

-###-

## When a pixel is not a pixel...

* In both cases, we'll consider an abstract "pixel" size when drawing the layout viewport, and map that to hardware pixels in the visual viewport
    * Layout viewport size is measured in "CSS pixels"

Note:
* Typical 1080p monitor (21-24") will be ~96 DPI
* Nexus 5X (5.2") is 421 DPI
* CSS pixels operate at about 96 DPI

-###-

## By default...

* A browser will attempt to show the entire layout viewport in the browser window
* The first tiny wikipedia page a few slides back
* How do we size the layout viewport appropriately?

-###-

## Meta viewport tags

* HTML `<meta>` tags are used to specify metadata that cannot be encoded in other tags
* With the development of their Retina displays, Apple started using the `<meta name="viewport" ...>` tag to instruct the browser on sizing the layout viewport to properly webpages formatted for mobile

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```


Note:
* that device-width will be fudged by devices, iPhone 6 advertises 375px width, has 750px wide display

-###-

## Great! But how to we build one page for all?

* CSS media queries
* Allow the developer to tailor the site to presentation on a variety of output media without changing the content
* Can be included in `<link>` tags to stylesheets, `@import` statements, or directly in css via `@media` tags

-###-

## Relevant Parameters

* Relevant for our case:
    * `max-width: 600px`
    * `min-width: 500px`
    * `orientation: landscape`
    * `orientation: portrait`

Note:
min/max width are layout viewport sizes

-###-

## Guidelines

* Use relative sizes
    * E.g., define the width of divs as a percentage of the page instead of a fixed pixel size, so it will scale across phones/tablets/laptops/desktops
* Start with the smallest needed size and define "breakpoints" as necessary

Note:
* Have the students count the breakpoints in the cultural district page
