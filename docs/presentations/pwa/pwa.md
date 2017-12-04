# Progressive Web Applications

-###-

## Twitter Lite

* [April 2017 Launch](https://lite.twitter.com/content/lite-twitter/en.html)
* A *progressive web application* to interact with Twitter
* Advertised benefits:
    * Tolerant of unreliable networks
    * Better performance on slower networks
    * Broken-up rendering work
        * Speed up initial paint to the browser window
        * Only render what is in the visual viewport
        * Defer rendering of non-critical items
    * Cut data usage

-###-

## Spotting a Progressive Web App

* Responsive
* Connectivity independent
    * Use service workers to run offline or on low-quality networks
* App-like
    * Separate the application functionality from content
* Fresh
    * Always up to date thanks to service worker update process
* Safe
    * Served via HTTPS

-###-

## Service Workers

* Background JavaScript acting as programmable network proxies
* They can't make synchronous calls such as to localStorage or synchronous XHRs
* They can't manipulate the DOM

-###-

## But What *can* They Do

* Give the JS application control of cache management
* Allow offline cache access
* Receive push notifications

-###-

## Where EventHandlers Fail

* Consider checking if an image load properly or not
* Image request might already have been processed by the time the event handler is defined
* In which case handler is never fired!
* We could check to see if the load successfully completed already
* But no way to check if the load had already been attempted and errored!

-###-

## Make Promises You Can Keep

```javascript
img1.ready().then(function() {
  // loaded
}, function() {
  // failed
});
```

```javascript
Promise.all([img1.ready(), img2.ready()]).then(function() {
  // all loaded
}, function() {
  // one or more failed
});
```

-###-

## Promise-based XHR

```javascript
function PXHR(url, resolve, reject) {
  return new Promise(function(resolve, reject) {
    var req = new XMLHttpRequest();
    req.open('GET', url);
    req.onreadystatechange = function() {
      if (req.readyState === XMLHttpRequest.DONE) {
        if (req.status === 200) { resolve(req.response); }
        else { reject(Error(req.statusText)); }
      }
    };
    req.send();
  });
}

PXHR('https://www.example.com', resolve, reject);
```