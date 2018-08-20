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

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Progressive
  * By definition, a progressive web app must work on any device and enhance progressively, taking advantage of any features available on the user’s device and browser.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Discoverable
  * Because a progressive web app is a website, it should be discoverable in search engines. This is a major advantage over native applications, which still lag behind websites in searchability.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Linkable
  * As another characteristic inherited from websites, a well-designed website should use the URI to indicate the current state of the application. This will enable the web app to retain or reload its state when the user bookmarks or shares the app’s URL.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Responsive
  * A progressive web app’s UI must fit the device’s form factor and screen size.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* App-like
  * A progressive web app should look like a native app and be built on the application shell model, with minimal page refreshes.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Connectivity-independent
  * It should work in areas of low connectivity or offline (our favorite characteristic).

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Re-engageable
  * Mobile app users are more likely to reuse their apps, and progressive web apps are intended to achieve the same goals through features such as push notifications.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Installable
  * A progressive web app can be installed on the device’s home screen, making it readily available.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Fresh
  * When new content is published and the user is connected to the Internet, that content should be made available in the app.

-###-

## [PWA Characteristics](https://www.smashingmagazine.com/2016/08/a-beginners-guide-to-progressive-web-apps/#characteristics-of-a-progressive-web-app)

* Safe
  * Because a progressive web app has a more intimate user experience and because all network requests can be intercepted through service workers, it is imperative that the app be hosted over HTTPS to prevent man-in-the-middle attacks.

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
