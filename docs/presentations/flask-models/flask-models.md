## Database Overview

* Our models are going to represent the state of a database that contains all of the data used by our web application
* We'll assume the use of transactional object-relational database management systems
    * MySQL, PostgreSQL, Oracle, SQLServer, etc.
* A transaction is a logical unit of work in DBMSs
* Examples:
    * Transferring money between bank accounts
    * Inventory updates

-###-

## ACID

* Atomicity
* Consistency
* Isolation
* Durability

-###-

## ACID - Atomicity

* <span class='fragment highlight-red' data-fragment-index='0'>A</span>tomicity
    * Either all the operations associated with a transaction happen or none of them happens

-###-

## ACID - Consistency

* <span class='fragment highlight-red' data-fragment-index='0'>C</span>onsistency Preservation
    * A transaction is a correct program segment. It satisfies the database’s integrity constraints at its boundaries

-###-

## ACID - Isolation

* <span class='fragment highlight-red' data-fragment-index='0'>I</span>solation
    * Transactions are independent, the result of the execution of concurrent transactions is the same as if transactions were executed serially, one after the other

-###-

## ACID - Durability

* <span class='fragment highlight-red' data-fragment-index='0'>D</span>urability (a.k.a. Permanency)
    * The effects of completed transactions become permanent surviving any subsequent failure(s)

-###-

## Data Tables

* In relational DBMSs, data is stored in tables
* The table rows are the records stored in the database, while the columns are the attributes of each record
* Based on the mathematical concept of a relation (a set of tuples)

-###-

## Data Tables

```
| Students                       |
|--------------------------------|
| Name    | ID     | Major | GPA |
|:--------|:-------|:------|:----|
| Alice   | 000001 | CS    | 4.0 |
| Bob     | 000002 | Math  | 3.2 |
| Charlie | 000003 | CS    | 2.7 |
| Denise  | 000004 | Film  | 3.7 |
```

-###-

## Relationships Between Tables

* Each table should have a `primary key`
    * Attribute that uniquely identifies each row
* `Foreign keys` are attributes that refer to rows in other tables

-###-

## Cardinality Ratios

* Cardinality ratios of relationships between tables must be carefully considered
* `1:1`
    * A person has a driver's license
* `1:n`
    * A movie has a director, but a director will make many movies
* `n:m`
    * A student enrolls in many classes and each class will have many students

-###-

## SQL

* Structured Query Language
* De facto query language for object-relational database management systems
* It is a `declarative` language
    * State what you want, not how to get it.

-###-

## SQL

```sql
SELECT *
FROM Students
WHERE GPA > 3.5;
```

-###-

## SQL Crash Course

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="http://recruitingdaily.com/wp-content/uploads/sites/6/2016/01/4746120-are-you-ready.gif" -->

Get Ready!!!

-###-

## SQL Crash Course

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="http://i51.tinypic.com/2eobgr6.gif" -->

Here it comes!!!

-###-

## SQL Crash Course

<!-- .slide: class="element-bkg" -->
<!-- .slide: data-background-image="https://media.giphy.com/media/xT5LMFfQQJtiKQ2gCs/giphy.gif" -->

-###-

## Object-Relational Mapping (ORM)

* Will map relational data (records from database tables) to objects that we can directly use within Python
* Glean all of the benefits provided by the data, all while writing only Pythonic code!

-###-

## SQLAlchemy

* Database abstraction toolkit and ORM
* We will use an extension to Flask that allows us to use SQLAlchemy's ORM within our Flask applications
* This is the "micro" part of Flask being a "microframework", no ORM by default

-###-

## Using SQLAlchemy within Flask

* An extension, so must be imported on its own:

```python
from flask_sqlalchemy import SQLAlchemy
```

* Must be tied to the flask app at initialization

Note:
The Flask-SQLAlchemy extension can be installed with: `pip install Flask-SQLAlchemy`

-###-

## Example model

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return "<User {}>".format(repr(self.username))
```

Note:
Note, constructor not needed
SQLAlchemy provides a constructor that takes keyword args for each column attribute
Can ignore ID:
```
>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
>>> ed_user.name
'ed'
>>> ed_user.password
'edspassword'
>>> str(ed_user.id)
'None'
```

After ed_user object is add()ed, and the commit()ed, its id attribute will be valid

Some definitions:
* `unique constraint`
* `commit`

* db state after additions?


-###-

## Example Model Actions

```python
a = User(username="admin", email="admin@example.com")
db.session.add(a)

p = User(username="peter", email="peter@example.org")
db.session.add(p)

g = User(username="guest", email="guest@example.com")
db.session.add(g)

db.session.commit()
```

Note:
* From the command line, run `export FLASK_APP=sql_example.py`
* `flask initdb`
* `flask shell`

-###-

## Querying Models

* Answering questions about data stored in the database
* Using SQLAlchemy, we will express such questions by chaining together calls to functions that produce SQLAlchemy Query objects

```python
entries = Entry.query.order_by(Entry.id).all()
```

-###-

## Querying Models

* In the example:
    * `Entry.query` returns Query object
    * `.orer_by(Entry.id)` returns Query object
    * `.all()` returns a `list`

```python
entries = Entry.query.order_by(Entry.id).all()
```

-###-

## Querying

```python
User.query.filter_by(username='peter').first()
# <User 'peter'>
```

```python
User.query.filter_by(username='missing').first()
# None
```

-###-

## Querying

```python
User.query.filter(User.email.endswith('@example.com')).all()
# [<User 'admin'>, <User 'guest'>]
```

```python
User.query.order_by(User.username)
# <flask_sqlalchemy.BaseQuery object at 0x109ee99e8>
```

-###-

## Querying

```python
User.query.order_by(User.username).all()
# [<User 'admin'>, <User 'guest'>, <User 'peter'>]
```

```python
User.query.all()
# [<User 'admin'>, <User 'peter'>, <User 'guest'>]
```

-###-

## Querying

```python
User.query.limit(1).all()
# [<User 'admin'>]
```

```python
User.query.get(1)
# <User 'admin'>
```

-###-

## Relationships

* SQLAlchemy provides constructs for easily accessing related models
* Through defining attributes using `db.relationship()`

-###-

## One-to-Many Relationships

```python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addresses = db.relationship('Address',
                                        backref='person',
                                        lazy='dynamic')

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    person_id = db.Column(db.Integer,
                                db.ForeignKey('person.id'))
```

Note:
one-to-one, add `uselist=False` to `relationship()`

-###-

## lazy-ness

* `select`
    * The default
    * SQLAlchemy will load the data as necessary in one go using a standard select statement
    * Loads when the parameter is accessed.
* `joined`
    * SQLAlchemy will load the relationship in the same query as the parent using a JOIN statement.
    * Loaded in initial query.

-###-

## lazy-ness

* `subquery`
    * Works like joined but instead SQLAlchemy will use a subquery
    * Loaded in initial query.
* `dynamic`
    * Instead of loading the items SQLAlchemy will return another query object which you can further refine before loading the items.
    * Must use something like `.all()` to access the list of data.

Note:
* A query object equivalent to a dynamic user.addresses relationship can be created using Address.query.with_parent(user)

-###-

## Many-to-Many relationship

```python
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
                    lazy='select',
                    backref=db.backref('pages', lazy='select'))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
```

Note:
* the use of db.backref allows us to set the lazy value of pages attribute as well
