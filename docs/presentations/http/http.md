## Steps to Look at a Page

* Step 1: Get a computer
* Step 2: ?
* Step 3: Profit

-###-

## Magic

![Magic](/images/http/magic.svg) <!-- .element: style="width:50%;" -->

Note:
* How do we get stuff to look at on the web?

-###-

# Gimme X

<!-- .slide: class="section-title" data-background="/lib/images/section-bkg.png" -->

Note:
* How do you say "Gimme X", theres a protocol for asking for things, its HTTP

-###-

## The HyperText Transfer Protocol

* Originally developed by Sir Tim
* HTTP v1.0 standard presented 1996
* HTTP/1.1 standard finalized in 1997
	* Via RFC 2068
	* Though improvements and updates in RFC 2616 (1999) essentially replace RFC 2068 as the definition of HTTP/1.1

-###-

## SPDY and HTTP/2.0

* In 2009, Google produced [SPDY](https://developers.google.com/speed/spdy/), another protocol for the transfer of web traffic
	* Doesn't replace HTTP, provides a tunnel for HTTP traffic
* In 2015, HTTP/2.0 standard was finalized
* Based around SPDY
* Google has since deprecated SPDY


Note:
* Why would Google want/need to invent a totally different web protocol?

-###-

## `GET`

* First method implemented
* HTTP now has several methods defined that specify the action that is requested to be performed on given resource
* Simply fetch the resource at some URL

-###-

## Host Attribute

```http
GET / HTTP/1.1
Host: www.toddwaits.org
User-Agent: curl/7.54.0
Accept: */*
```

Note:
* So the host says: go here, right?
    * No.

-###-

## Getting an HTTP Request to a Webserver

* Physical Layer <!-- .element: class="fragment highlight-magenta" data-fragment-index="3" -->
* Data Link Layer <!-- .element: class="fragment highlight-magenta" data-fragment-index="3" -->
* Network Layer <!-- .element: class="fragment highlight-orange" data-fragment-index="2" -->
* Transport Layer <!-- .element: class="fragment highlight-yellow" data-fragment-index="1" -->
* Session Layer <!-- .element: class="fragment highlight-cyan" data-fragment-index="0" -->
* Presentation Layer <!-- .element: class="fragment highlight-cyan" data-fragment-index="0" -->
* Application Layer <!-- .element: class="fragment highlight-cyan" data-fragment-index="0" -->

<!-- .element: class="column-left" -->

* Application <!-- .element: class="fragment highlight-cyan" data-fragment-index="0" -->
* Transport <!-- .element: class="fragment highlight-yellow" data-fragment-index="1" -->
* Internet <!-- .element: class="fragment highlight-orange" data-fragment-index="2" -->
* Link Layer <!-- .element: class="fragment highlight-magenta" data-fragment-index="3" -->

<!-- .element: class="column-right" -->

Note:
* Physical Layer
    * "Ethernet cables and Token Ring networks. Additionally, hubs and other repeaters are standard network devices that function at the Physical layer, as are cable connectors."
* Data Link Layer
    * the Data Link layer checks for physical transmission errors and packages bits into data "frames".
* Network Layer
    * When data arrives at the Network layer, the source and destination addresses contained inside each frame are examined to determine if the data has reached its final destination. If the data has reached the final destination, this Layer 3 formats the data into packets delivered up to the Transport layer. Otherwise, the Network layer updates the destination address and pushes the frame back down to the lower layers.
* Transport Layer
    * Different transport protocols may support a range of optional capabilities including error recovery, flow control, and support for re-transmission. (TCP, ftp, utp)
    * FTP vs HTTP
        * Given all details on this page. What makes FTP faster:
            * No added meta-data in the sent files, just the raw binary
            * Never chunked encoding "overhead"
        * What makes HTTP faster:
            * reusing existing persistent connections make better TCP performance
            * pipelining makes asking for multiple files from the same server faster
            * (automatic) compression makes less data get sent
            * no command/response flow minimizes extra round-trips
* Session Layer
    * manages the sequence and flow of events that initiate and tear down network connections.
* Presentation Layer
    * handles syntax processing of message data such as format conversions and encryption / decryption
* Application Layer
    * The Application layer supplies network services to end-user applications
    * Client side: Browser
    * Server side: Nginx, backend application

-###-

## HTTP Route

```bash
 1  pod-w-vl75.gw.cmu.net (128.237.128.1)  12.768 ms  467.251 ms  129.222 ms
 2  core0-pod-w-cyh.gw.cmu.net (128.2.0.241)  1.501 ms  2.032 ms  1.529 ms
 3  pod-i-cyh-core0.gw.cmu.net (128.2.0.250)  1.491 ms  2.224 ms  2.284 ms
 4  te0-0-2-1.nr11.b015486-1.pit02.atlas.cogentco.com (38.140.44.153)  2.615 ms  2.300 ms  2.332 ms
 5  154.24.42.97 (154.24.42.97)  2.279 ms
    154.24.50.197 (154.24.50.197)  2.092 ms
    154.24.42.97 (154.24.42.97)  2.123 ms
 6  be2821.ccr21.cle04.atlas.cogentco.com (154.54.83.117)  5.458 ms
    be2822.ccr22.cle04.atlas.cogentco.com (154.54.83.157)  5.570 ms
    be2821.ccr21.cle04.atlas.cogentco.com (154.54.83.117)  5.631 ms
 7  be2717.ccr41.ord01.atlas.cogentco.com (154.54.6.221)  12.279 ms
    be2718.ccr42.ord01.atlas.cogentco.com (154.54.7.129)  12.996 ms
    be2717.ccr41.ord01.atlas.cogentco.com (154.54.6.221)  12.799 ms
 8  be2832.ccr22.mci01.atlas.cogentco.com (154.54.44.169)  27.914 ms  24.612 ms
    be2831.ccr21.mci01.atlas.cogentco.com (154.54.42.165)  33.557 ms
 9  be2433.ccr32.dfw01.atlas.cogentco.com (154.54.3.213)  34.090 ms
    be2432.ccr31.dfw01.atlas.cogentco.com (154.54.3.133)  34.488 ms  34.073 ms
10  be2561.rcr21.b010621-0.dfw01.atlas.cogentco.com (154.54.6.74)  35.314 ms
    be2560.rcr21.b010621-0.dfw01.atlas.cogentco.com (154.54.5.238)  35.476 ms  35.303 ms
11  38.122.58.34 (38.122.58.34)  35.189 ms  35.120 ms  34.693 ms
12  207.210.229.6 (207.210.229.6)  36.106 ms  34.632 ms  34.471 ms
13  174.136.31.214 (174.136.31.214)  56.230 ms  44.195 ms  35.830 ms
14  sansa.asoshared.com (143.95.33.24)  34.662 ms  34.314 ms  34.773 ms
```

Note:
* <https://www.youtube.com/watch?v=SXmv8quf_xM>

-###-

## HTTP Response

```http
HTTP/1.1 200 OK
Server: nginx
Date: Tue, 19 Sep 2017 18:35:50 GMT
Content-Type: text/html
Content-Length: 8537
Connection: keep-alive
Keep-Alive: timeout=15
Vary: Accept-Encoding
Last-Modified: Fri, 01 Jan 2016 14:38:49 GMT
ngpass_ngall: 1
Accept-Ranges: bytes

<!--HTML CONTENT-->
```

-###-

## `POST`

* Attaches data with the request that should be handled by the specified resource
    * The result of a web form
    * A new entry to add to a database

-###-

## `PUT`

* Attaches data that should be placed at the specified resource
* If the resource does not currently exist, specified data should not be that resource identified by the given URL

-###-

## `PUT` Sounds Dangerous

* Safe HTTP methods
    * Should only request a resource, should not change the state of the server
    * GET is (by convention) a safe method
* POST and PUT are intended to cause side-effects (i.e., change the state of the server)

-###-

## Works in Theory

> In theory, there is no difference between theory and practice.

**Yogi Berra**

-###-

## Breaks in Practice

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="https://media.tenor.com/images/06681b2ec4eb5ac1873c90d01f9a097e/tenor.gif" -->

* `scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]`
* The URL **query string** can be used to affect server state
* `http://example.com/storefront?user=nick&newitem=laptop`
    * Could be used by the example.com webstore app to have me request to buy a laptop
    * This is BAD

-###-

## HTTP Methods

* `GET`
* `POST`
* `PUT`
* `DELETE`
    * Delete listed resource

Note:
* POST
    * Sends info to the Server to act on.
    * Can create, but generally shouldn't (idempotent)
    * returns response, but not required to send much else
* PUT
    * Like POST
    * since PUT is idempotent, you must send all possible values.
    * get the same response (everything) all the time
* DELETE
    * The DELETE method deletes the specified resource.

-###-

## HTTP Safe Methods

* `HEAD`
    * Like `GET`, but returns headers only, no body
* `OPTIONS`
    * Gets a list of methods supported by the destination server
* `TRACE`
    * Like `GET`, but returns changes made to the request as it travels through the network

-###-

## Comparisons of HTTP Methods

```markdown
| HTTP Method | RFC      | Request Has Body | Response Has Body | Safe | Idempotent | Cacheable |
|:------------|:---------|:-----------------|:------------------|:-----|:-----------|:----------|
| GET         | RFC 7231 | No               | Yes               | Yes  | Yes        | Yes       |
| HEAD        | RFC 7231 | No               | No                | Yes  | Yes        | Yes       |
| POST        | RFC 7231 | Yes              | Yes               | No   | No         | Yes       |
| PUT         | RFC 7231 | Yes              | Yes               | No   | Yes        | No        |
| DELETE      | RFC 7231 | No               | Yes               | No   | Yes        | No        |
| CONNECT     | RFC 7231 | Yes              | Yes               | No   | No         | No        |
| OPTIONS     | RFC 7231 | Optional         | Yes               | Yes  | Yes        | No        |
| TRACE       | RFC 7231 | No               | Yes               | Yes  | Yes        | No        |
| PATCH       | RFC 5789 | Yes              | Yes               | No   | No         | No        |
```

Note:
* CONNECT
    * The CONNECT method converts the request connection to a transparent TCP/IP tunnel, usually to facilitate SSL-encrypted communication (HTTPS) through an unencrypted HTTP proxy. See HTTP CONNECT tunneling.
* PATCH
    * The PATCH method applies partial modifications to a resource.
* Idempotent
    * From a RESTful service standpoint, for an operation (or service call) to be idempotent, clients can make that same call repeatedly while producing the same result.

-###-

## HTTP Status Codes

* 200
    * OK
* 301
    * Moved Permanently
* 400
    * Bad Request

-###-

## HTTP Status Codes

* 403
    * Forbidden
* 404
    * Not Found
* 500
    * Internal Server Error

-###-

## Networked Infrastructure

![Magic](/images/http/networking.svg) <!-- .element: style="width:50%;" -->

-###-

## Backend Application Stack

![Python](/images/http/python-512.png) <!-- .element: style="width:20%;" -->
![SQLite](https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Sqlite-square-icon.svg/2000px-Sqlite-square-icon.svg.png) <!-- .element: style="width:20%;" -->
![Flask](https://cdn.tutsplus.com/net/authors/jeffreyway/flask.jpg)
