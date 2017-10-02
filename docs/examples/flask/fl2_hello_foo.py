from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Oh! Hello again!"

@app.route("/foo")
def fooController():
	return "<h1>THIS IS THE FOO PAGE</h1>"

@app.route("/bar/")
def bar():
	return "<h1>this is the bar page</h1>"
	
if __name__ == "__main__":
	app.run()
