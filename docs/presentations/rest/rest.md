## Beatiful

> When the web was designed the designers did a really good job

##### Roy Fielding

-###-

## What properties does the web exhibit?

* Resources exist and can be globally identified?
    * URLs
* Representations of these resources are exchanged by clients and servers
    * HTML pages, JSON
* Standard interfaces are used for communication
    * HTTP

-###-

## Stateless

* It should not matter to clients if they are directly connected to a server or there are caches, NAT, other layers in between
* Client/server communications should be stateless

-###-

## Building large scale networked systems is hard

* So let's take those properties about the web and use that as the basis of an architectural style
* Representational State Transfer
    * Systems that follow the same architectural principles are said to be RESTful

-###-

## Representational State Transfer (REST)

* An application should be able to interact with a resource with only the following knowledge:
    * The identifier of the resource
    * The action to be performed
    * An understanding of the representation returned

-###-

## Simple Interfaces

* `GET`
* `POST`
* `PUT`
* `DELETE`
* -NOT-
    * `getUsers()`
    * `getNewUsersSince(date SinceDate)`
    * `savePurchaseOrder(string CustID, string PurchaseOrderID)`

Note:
* How do we even utilize PUT/DELETE??
* web forms can only GET/POST...

-###-

## Interface to a collection

* `http://example.com/resources`
* `GET`
    * List the URIs and perhaps other details of the collection's members
* `PUT`
    * Replace the entire collection with another collection

-###-

## Interface to a collection

* `POST`
    * Create a new entry in the collection. The new entry's URI is assigned automatically and is usually returned by the operation
* `DELETE`
    * Delete the entire collection.

-###-

## Nouns, not verbs

```
http://localhost/projects
http://localhost/getprojects
```

```
GET     http://localhost/getprojects
POST    http://localhost/getprojects
PUT     http://localhost/getprojects
DELETE  http://localhost/getprojects
```

-###-

## Nouns, not verbs

```
http://localhost/projects
http://localhost/getprojects
```

```
GET     http://localhost/projects
POST    http://localhost/projects
PUT     http://localhost/projects
DELETE  http://localhost/projects
```

-###-

## Interface to an item in a collection

* `http://example.com/resources/item37`
* `GET`
    * Retrieve a representation of the addressed member of the collection, expressed in an appropriate Internet media type
* `PUT`
    * Replace the addressed member of the collection, or if it doesn't exist, create it

-###-

## Interface to an item in a collection

* `POST`
    * Not generally used
* `DELETE`
    * Delete the addressed member of the collection.

-###-

## Query Strings to Reduce Complexity

```
http://localhost/projects/client/acme/
http://localhost/projects/?client=acme
http://localhost/projects/?client=acme&fields=client,name,team
```

-###-

## REST Request 1

```
POST /classScedService HTTP/1.1
<openClassRequest term="SUM2016" class="CS1520"/>
```

-##-

## REST Response 1

```
HTTP/1.1 200 OK

<openClassList>
    <class number="CS1520" time="930" />
    <class number="CS1520" time="1430" />
</openClassList>
```

-##-

## Rest Request 2

```
POST /classScedService HTTP/1.1

<registerRequest>
    <class number="CS1520" time="1430" />
    <student id = "alice"/>
</registerRequest>
```

-##-

## REST Response 2

```
HTTP/1.1 200 OK
<registration>
    <class number="CS1520" time="1430" />
    <student id="alice"/>
</registration>
```

```
HTTP/1.1 200 OK

<registrationFailure>
    <class number="CS1520" time="1430" />
    <student id="alice"/>
    <reason>Full Class</reason>
</registrationFailure>
```

-###-

## Better Reporting Request 1

```
GET /classes/SUM2016?status=open HTTP/1.1
```

-##-

## Better Reporting Response 1

```
HTTP/1.1 200 OK

<openClassList>
    <class id=123 number="CS1520" time="930" />
    <class id=124 number="CS1520" time="1430" />
</openClassList>
```

-##-

## Better Reporting Request 2

```
POST /registration/124 HTTP/1.1

<registerRequest>
    <student id = "alice"/>
</registerRequest>
```

-##-

## Better Reporting Response 2

```
HTTP/1.1 201 CREATED Location=/registrations/124/registration44

<registration>
    <class id=124 number="CS1520" time="1430" />
    <student id="alice"/>
</registration>
```

```
HTTP/1.1 409 CONFLICT

<openClassList>
    <class id=123 number="CS1520" time="930" />
</openClassList>
```

Note:
* Address 201 suggestion from the other lecture
* We weren't actually creating a new resource
* we pushed data to the server, and that data may be included in generating a representation of some resource, but it was not a new resource

-###-

## Alright, NOW we're RESTful, right?

* How does the client know that `/registration/124` is the URI for registering for class id 124?
    * This wasn't mentioned in the `openClassList` response
    * Violates our assumption of what the client should need to know to interact with our system!

-###-

## HATEOAS

* Hypermedia as the Engine of Application State
* Clients should interact with a network application entirely through hypermedia provided dynamically by application servers
    * No prior knowledge of application interaction required

-###-

## HATEOAS Request 1

```
GET /classes/SUM2016?status=open HTTP/1.1
```

-##-

## HATEOAS Response 1

```
HTTP/1.1 200 OK

<openClassList>
    <class id=123 number="CS1520" time="930">
        <link rel = "/linkrels/class/register"
              uri = "/registrations/123"/>
    </class>
    <class id=124 number="CS1520" time="1430">
        <link rel = "/linkrels/class/register"
              uri = "/registrations/124"/>
    </class>
</openClassList>
```

-##-

## HATEOAS Request 2

```
POST /registration/124 HTTP/1.1

<registerRequest>
    <student id = "alice"/>
</registerRequest>
```

-##-

## HATEOAS Response 2

```
HTTP/1.1 201 CREATED Location=/registrations/124/registration44

<registration>
    <class id=124 number="CS1520" time="1430" />
    <student id = "alice"/>
    <link rel = "/linkrels/registration/drop"
          uri = "/registrations/124/registration44"/>
    <link rel = "/linkrels/registration/setgradeoption"
          uri = "/registrations/124/registration44/gradeOpt"/>
</registration>
```

-###-

## Why HATEOAS?

* Assume clients enter your app through a simple fixed URL
* Alice could have just gone to registrar.pitt.edu
* All future actions the client may take are discovered within resource representations returned from the server

-###-

## Why HATEOAS?

* All that’s needed is basic knowledge of hypermedia
* Alice could be given the link to a list of open classes from the registrar index resource, leading to the previous examples
* Further, the registrar could update how the registration application works, but Alice wouldn't have to update her client to respect these changes

-###-

## Something something theory and practice

* Applications that call themselves RESTful may actually fall somewhere in between these examples
* May even basically embody the first example...
* Dumb pipes, smart endpoints

Note:
* hateoas is kind of a pain...
    * why?
        * alot of work to build up serverside map
        * alot of work to traverse map from server
    * noone wins!
* so why bother with hateoas?
    * often people wont
* so why bother with rest??
    * tie back to building web apps, not web sites
    * further, building apps that work across web, mobile (android, ios) ...
