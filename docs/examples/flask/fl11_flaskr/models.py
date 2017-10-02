from flask_sqlalchemy import SQLAlchemy

# note this should only be created once per project
# to define models in multiple files, put this in one file, and import db into each model, as we import it in flaskr.py
db = SQLAlchemy()

class Entry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	text = db.Column(db.Text, nullable=False)

	def __init__(self, title, text):
		self.title = title
		self.text = text

	def __repr__(self):
		return '<Entry {}>'.format(self.id)
