# Copyright 2015, Kevin Burke, Kyle Conroy, Ryan Horn, Frank Stratton, Guillaume Binet
# Created as documentation for Flask-RESTful Flask extension

from flask import Flask, render_template

app = Flask(__name__)

#app.config.update(dict(SEND_FILE_MAX_AGE_DEFAULT=0))

@app.route("/")
def root_page():
	return render_template("homepage.html")

if __name__ == '__main__':
	app.run()
