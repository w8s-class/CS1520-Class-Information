from flask import Flask
from flask_sqlalchemy import SQLAlchemy

### init

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

### models

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email
		
	def __repr__(self):
		return '<User %r>' % self.username

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	addresses = db.relationship('Address', backref='person', lazy='dynamic')
	
	def __init__(self, name):
		self.name = name

class Address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50))
	person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

	def __init__(self, email):
		self.email = email

tags = db.Table('tags',
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
	db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	tags = db.relationship('Tag', secondary=tags, backref=db.backref('pages', lazy='dynamic'))

	def __init__(self, name):
		self.name = name

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

	def __init__(self, name):
		self.name = name
		
### controllers

def displayResult(num, res):
	print("\nQ{}:\n".format(num), res, "\n\n")
		
@app.cli.command('initdb')
def initdb_command():
	"""Reinitializes the database"""
	db.drop_all()
	db.create_all()

	# populate users
	db.session.add(User("admin", "admin@example.com"))
	db.session.add(User("peter", "peter@example.org"))
	db.session.add(User("guest", "guest@example.com"))

	# populate 1-N example
	nick = Person("Nick")
	db.session.add(nick)
	nick.addresses.append(Address("nlf4@pitt.edu"))

	cs_addr = Address("nlf4@cs.pitt.edu")
	db.session.add(cs_addr)
	cs_addr.person = nick

	# populate M-N example
	p1 = Page("p1")
	t1 = Tag("t1")
	t2 = Tag("t2")
	t3 = Tag("t3")
	
	db.session.add(p1)
	p1.tags.append(t1)
	p1.tags.append(t2)
	p1.tags.append(t3)

	p2 = Page("p2")
	t1.pages.append(p2)
	t2.pages.append(p2)
	t2.pages.append(Page("p3"))
	
	# commit
	db.session.commit()
	print('Initialized the database.')

		
@app.cli.command('check')
def default():
	"""demonstrates model queries and relationships"""
	# queries
	displayResult(1, User.query.filter_by(username='peter').first())
	displayResult(2, User.query.filter_by(username='missing').first())
	displayResult(3, User.query.filter(User.email.endswith('@example.com')).all())
	displayResult(4, User.query.order_by(User.username))
	displayResult(5, User.query.order_by(User.username).all())
	displayResult(6, User.query.all())
	displayResult(7, User.query.limit(1).all())
	tmp = User.query.get(1)
	displayResult(8, tmp)
	print(tmp.id)
	displayResult(9, User.query.filter(User.id < 3).all())
	displayResult(10, User.query)

	# 1-N example
	print("\n\nperson:")
	per = Person.query.first()
	print("\tname:", per.name)
	print("\taddresses object:", per.addresses)
	print("\taddresses:")
	for a in per.addresses:
		print("\t\t", a.email)

	print("\n\nemails:")
	eml = Address.query.all()
	for e in eml:
		print("\taddr", e.email, ";  owner", e.person.name)

	# M-N example
	print("\n\npages:")
	pages = Page.query.all()
	for p in pages:
		print("\tname:", p.name)
		for t in p.tags:
			print("\t\ttag:  ", t.name)
	
	print("\n\ntags:")
	tags = Tag.query.all()
	for t in tags:
		print("\tname:", t.name)
		for p in t.pages:
			print("\t\tpage:  ", p.name)
