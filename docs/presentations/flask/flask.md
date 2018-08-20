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
    * fl2
    * fl3
    * fl4
    * fl5
* how can you possibly POST to profile/alice???
* `curl --data "user=alice&pass=qwerty" 127.0.0.1:5000/profile/alice`
* discuss differences between loginForm/redirect
* note that redirect triggers a GET with Chrome
* note the information leaked by returnCodes
    * not trying to dig into web security too much right now...

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
