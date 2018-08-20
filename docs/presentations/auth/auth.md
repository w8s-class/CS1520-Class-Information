## Access control vs. authentication

* We want to control how users can interact with information
    * Users should only be able to view their own messages
    * Users can only update their own passwords
    * This is ***access control***
    * What actions is a subject allowed to take on a given object?
* How do we determine the who a user is?
    * This is ***authentication***
    * The binding of an identity to a subject

-###-

## General approaches to authentication

* Verify identity based on:
    * Something the user knows
        * password, PIN
    * Something the user has
        * ATM card, smart card
    * Something the user is
        * fingerprints, retinal scans

-###-

## General approaches to authentication

* Using multiple of these together leads to two-factor authentication
* Password authentication is (currently) the most widely-used authentication approach

-###-

## Using passwords in web applications

* Up until this point, we have used HTML forms to gather and submit usernames/passwords to the server, and then set a cookie (returned with all requests) to flag the user as "logged in"
    * Where is this approach going to fall short?

Note:
* What about using a non-browser client?
    * cURL?
    * phone apps?

-###-

## HTTP basic authentication

* Send username and password along with the HTTP header
    * Via the Authorization field of the header.

-###-

## HTTP basic authentication

```http
GET / HTTP/1.1
Host: cs.pitt.edu
Authorization: Basic Laha9aDS8n3q8bv
#Field Name    #Type #data
...
```

-###-

## HTTP basic authentication

* Username and password are concatenated together with a single ":" and then Base64 encoded

Note:
* there are multiple types of Authorizations possible with HTTP
    * [digest](https://en.wikipedia.org/wiki/Digest_access_authentication) is one
    * [AWS4-HMAC-SHA256](http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html) was made up by amazon because they weren't happy with existing options

-###-

## Base64 Encoding

* Representing data as a sequence of base 64 numbers
    * `0-25 : A-Z`
    * `26-51 : a-z`
    * `52-61 : 0-9`
    * `62 : +`
    * `63 : /`
* To convert 8-bit encoded string to Base64, grab 3 bytes of input, turn it into 4 output characters
* If only 1 or 2 bytes left, pad out Base64 output with =

-###-

## Grabbing basic HTTP auth in Flask

* Would be nice to be able to do something like this?
* How could we implement `@requires_auth`?

```python
@app.route('/secret-page')
@requires_auth
def secret_page():
    return render_template('secret_page.html')
```

-###-

## `@requires_auth` Decorator

```python
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        if not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
```

-###-

## Helper Functions

```python
def check_auth(username, password):
    return username == 'admin' and password == 'secret'
```

```python
def authenticate():
    """Sends a 401 response that enables basic auth"""
     return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})
```

-###-

## Token Authentication

* Have user acquire token and then send that along with requests.
    * E.g., you can access GitHub's API by sending a token along with your request header:
    * `Authorization: token 798as7vy098yh2198v7asd7...`
* Why is this helpful?

-###-

## OAuth

* Allows a user to authorize a web app to access their some of their data on another service

![OAuth](https://i.stack.imgur.com/bzRSr.png)

-###-

## OpenID

* An approach to federated authentication
* Allows the user gather proof that they are the owner of some identity on another site
    * Does not delegate access to the user's data on that other site, however.
* Can be used to authenticate a user to get an OAuth token
