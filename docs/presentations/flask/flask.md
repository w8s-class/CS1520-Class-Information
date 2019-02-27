## What is Flask?

* A micro web framework written in Python
* First release was in 2010
    * Current version (1.0.2) was released in May 2018
* Currently powers LinkedIn and Pinterest (parts at least)

-###-

## Hello, Flask!

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

Note:
* starts server at 127.0.0.1:5000
* Examples:
    * fl1
* how can you possibly POST to profile/alice???
* `curl --data "user=alice&pass=qwerty" 127.0.0.1:5000/profile/alice`
* discuss differences between loginForm/redirect
* note that redirect triggers a GET with Chrome
* note the information leaked by returnCodes
    * not trying to dig into web security too much right now...

-###-

## Flask Routes

* Use `@app.route` decorator to connect HTTP route to Python function
* A route defines the URL
* The function is what *happens* when a client requests that URL
* Flask is an HTTP web application-- not working with static resources.
* Default HTTP method is `GET`

Note:
* fl2
* How does Flask handle the routes `/foo` and `/bar/` differently?
  * Looking at `Networking` console in Chrome, check HTTP status code for `/bar` vs `/bar/`
  * Check the difference between `/foo` and `/foo/`

-###-

## Flask Forms and `POST` vs `GET`

* Use the `@app.route` decorator to specify additional methods to support.
* HTML attaches form data to the body of the HTTP request in key value pairs.
  * `anumber=1&astring=dog`
  * The key's derive their name from the `name` attribute in the `input` element in the HTML `form`.
  * `<input type="text" name="astring" />`
* In Flask, access form data with `request.form[key]` or `request.form.get(key)`

Note:
* fl3
* What's the difference between `request.form[key]` and `request.form.get(key)`
* Where does the `request` object come from? Imports!

-###-

## Flask "Login"

```python
users[request.form["user"]] == request.form["pass"]
```

* Using the value of `request.form["user"]` as the key for the `users` dictionary to compare the user's password in the dictionary to the value passed from the browser in the `request.form["pass"]`
* What does `abort(404)` do?
* Why are there two decorators for the `profile` function?

Note:
* fl4
* Double decorator?

```python
@app.route("/profile/", methods=["GET", "POST"])
@app.route("/profile/<username>", methods=["GET", "POST"])
```

-###-

## Flask Redirects

* The `redirect()` takes a URL as an argument.
  * Issues a `302` HTTP Status code and tells the browser to initiate a `GET` request on the URL passed in.
* The argument for `url_for()` is the name of the **function**.
  * Returns a string URL.

Note:
* fl5
* The argument for `url_for` is the name of the **FUNCTION**, not the path to the route.

-###-

## Cookies

* Small pieces of data authored by an HTTP server and stored on the client's machine
    * Well, that was the original intent, but also editable from JS
    * This was used as a hacky way to implement client side storage before HTML
    * Do we want clients to be able to edit cookies authored by our site?

-###-

## Flask Sessions

* Allows access to cookie data in such a way that if the cookie is changed by the user, Flask will see this disregard the session data
* Does this by establishing a secret key in the Flask app
* Only someone who knows the secret can modify the session data
    * Note: anyone can *read* the data, sessions just protect from *unauthorized modification*

Note:
* Example:
    * fl6
* Make note of the `app.secret_key = "this is a terrible secret key"`
  * Does not work without that!
* Note how our HTML variables are getting really unwieldy...
    * As is our "database"

-###-

## Model - View - Controller (MVC)

![MVC](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/1200px-MVC-Process.svg.png)

Note:
* User uses controller
* Controller manipulates model
* Model updates view
* View is shown to the user
* Very useful paradigm for UI design


-###-

## Model

* Model
    * Handles interaction with stored data
    * We'll use an abstraction off of SQLite as our model

-###-

## Controller

* Controller
    * The decorated code you've seen up until this point

-###-

## View

* View
    * Represents what is displayed to the user
    * We'll use templates of HTML files that are populated with data from our model
