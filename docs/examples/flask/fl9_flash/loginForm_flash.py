from flask import Flask, request, abort, url_for, redirect, session, render_template, flash

app = Flask(__name__)

users = {"alice":"qwert", "bob":"asdfg", "charlie":"zxcvb"}

# by default, direct to login
@app.route("/")
def default():
	return redirect(url_for("logger"))
	
@app.route("/login/", methods=["GET", "POST"])
def logger():
	# first check if the user is already logged in
	if "username" in session:
		flash("Already logged in!")
		return redirect(url_for("profile", username=session["username"]))

	# if not, and the incoming request is via POST try to log them in
	elif request.method == "POST":
		if request.form["user"] in users and users[request.form["user"]] == request.form["pass"]:
			session["username"] = request.form["user"]
			flash("Successfully logged in!")
			return redirect(url_for("profile", username=session["username"]))
		else:
			flash("Error logging you in!")

	# if all else fails, offer to log them in
	return render_template("loginPage.html")

@app.route("/profile/")
def profiles():
	return render_template("profiles.html", users=users)

@app.route("/profile/<username>")
def profile(username=None):
	if not username:
		return redirect(url_for("profiles"))
			
	elif username in users:
		# if specified, check to handle users looking up their own profile
		if "username" in session:
			if session["username"] == username:
				return render_template("curProfile.html")

		return render_template("otherProfile.html", name=username)
			
	else:
		# cant find profile
		abort(404)

@app.route("/logout/")
def unlogger():
	# if logged in, log out, otherwise offer to log in
	if "username" in session:
		# note, here were calling the .clear() method for the python dictionary builtin
		session.clear()
		# flashes are stored in session["_flashes"], so we need to clear the session /before/ we set the flash message!
		flash("Successfully logged out!")
		# we got rid of logoutpage.html!
		return redirect(url_for("profiles"))
	else:
		flash("Not currently logged in!")
		return redirect(url_for("logger"))

# needed to use sessions
# note that this is a terrible secret key
app.secret_key = "this is a terrible secret key"
			
if __name__ == "__main__":
	app.run()

