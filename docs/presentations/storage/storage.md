## Javascript File I/O

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="https://media.giphy.com/media/TbUMPa2py8UVi/giphy.gif" -->

Tell me a story about Javascript and File I/O

-###-

## Javascript File I/O

* There is no File I/O in Javascript

Note:
* Why?
	* Running on the browser, not the host machine
	* Sandboxing
	* Security
* Things we need to talk about:
	* Sending information back to web
		* At all
		* From JS
* <https://developer.mozilla.org/en-US/docs/Web/API/File>
	* <http://caniuse.com/#feat=filesystem>

-###-

## Storage

* As part of HTML5, an API for Web Storage was proposed
	* Has the browser allocate space for JS apps to store data on the client machine
	* Amount available per domain varies by browser
	* < 4MB is a good rule of thumb
	* Data is stored as key/value pairs
	* Both strings

-###-

## Storage

* Two implementations of this API are available to JS apps:
	* `localStorage`
	* `sessionStorage`

-###-

# `localStorage`

<!-- .slide: class="section-title" data-background="/lib/images/section-bkg.png" -->

-###-

## `localStorage`

* `localStorage.length`
	* Read only value
	* Number of key/value pairs stored in localStorage

-###-

## `localStorage`

* `localStorage.getItem(key)`
* `localStorage.setItem(key, value)`
* `localStorage.removeItem(key)`
* `localStorage.key(index)`
	* For a given `index` n, return the nth `key` in `localStorage`
* `localStorage.clear()`
	* Remove all key/value pairs from `localStorage`

Note:
* [js12](https://w8s-class.github.io/CS1520-Class-Information/examples/js/js12_storage.html)
* Note that order of keys is lexicographical
* Change up to use key(i) when loading data, note differences
* Data saved in storage under http, will be inaccessible via https

-###-

# `sessionStorage`

<!-- .slide: class="section-title" data-background="/lib/images/section-bkg.png" -->

-###-

## `sessionStorage`

* Has the same API as `localStorage`
	* Both implement `Storage`
* However, sessionStorage is cleared as soon as the session on the current page is ended
	* The browser window/tab is closed
	* When the same page is loaded in a different window/tab, a new session is created
* Why would you use sessionStorage as opposed to simple variable storage?


Note:
* `sessionStorage` survives multiple page loads
* "Opening a page in a new tab or window will cause a new session to be initiated, which differs from how session cookies work."
* Gulp task that failed due to in-memory variables.
