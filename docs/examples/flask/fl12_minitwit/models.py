from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(24), nullable=False)
	email = db.Column(db.String(80), nullable=False)
	pw_hash = db.Column(db.String(64), nullable=False)

	messages = db.relationship('Message', backref='author')

	follows = db.relationship('User', secondary='follows', 
	  primaryjoin='User.user_id==follows.c.follower_id', 
	  secondaryjoin='User.user_id==follows.c.target_id', 
	  backref=db.backref('followed_by', lazy='dynamic'), 
	  lazy='dynamic')
	
	def __init__(self, username, email, pw_hash):
		self.username = username
		self.email = email
		self.pw_hash = pw_hash

	def __repr__(self):
		return '<User {}>'.format(self.username)

follows = db.Table('follows',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('target_id', db.Integer, db.ForeignKey('user.user_id'))
)

class Message(db.Model):
	message_id = db.Column(db.Integer, primary_key=True)
	author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
	text = db.Column(db.Text, nullable=False)
	pub_date = db.Column(db.Integer)

	def __init__(self, author_id, text, pub_date):
			self.author_id = author_id
			self.text = text
			self.pub_date = pub_date

	def __repr__(self):
			return '<Message {}'.format(self.message_id)
