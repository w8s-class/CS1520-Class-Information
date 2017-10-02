# -*- coding: utf-8 -*-
"""
	Flaskr
	~~~~~~

	A microblog example application written as Flask tutorial with
	Flask and sqlite3.

	:copyright: (c) 2015 by Armin Ronacher.
	:license: BSD, see LICENSE for more details.

	Updated by Nick Farnan 2016
"""

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

from models import db, Entry


# create our little application :)
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default',

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'flaskr.db')
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

db.init_app(app)


@app.cli.command('initdb')
def initdb_command():
	"""Creates the database tables."""
	db.drop_all()
	db.create_all()
	print('Initialized the database.')

	
@app.route('/')
def show_entries():
	entries = Entry.query.order_by(Entry.id.desc()).all()
	return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	new = Entry(request.form['title'], request.form['text'])
	db.session.add(new)
	db.session.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('You were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))
