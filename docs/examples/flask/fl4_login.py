from flask import Flask, request, abort, url_for, redirect

app = Flask(__name__)

users = {"alice":"qwert", "bob":"asdfg", "charlie":"zxcvb"}

loginPage = """<!DOCTYPE html>
<html>
	<head>
		<title>Basic form</title>
	</head>
	<body>
		<form action="{}" method="post">
			Username:  <input type="text" name="user" />
			<br />
			Password:  <input type="text" name="pass" />
			<br />
			<input type="submit" value="submit" />
		</form>
	</body>
</html>
"""

curProfile = """<!DOCTYPE html>
<html>
	<head>
		<title>Your profile!</title>
	</head>
	<body>
		Welcome back!
	</body>
</html>
"""

otherProfile = """<!DOCTYPE html>
<html>
	<head>
		<title>{0}'s profile!</title>
	</head>
	<body>
		This is {0}'s profile page.
	</body>
</html>
"""


@app.route("/")
def default():
	return redirect(url_for("login"))
	
@app.route("/login/")
def login():
	return loginPage.format(url_for("profile"))

@app.route("/profile/", methods=["GET", "POST"])
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username=None):
	if request.method == "POST":

		if not username:
			if users[request.form["user"]] == request.form["pass"]:
				return curProfile
			else:
				abort(401)

		elif username in users:
			return redirect(url_for("profile", username=request.form["user"]))

		else:
			abort(404)
	else:
		if username and username in users:
			return otherProfile.format(username)
		else:
			abort(404)
	
	
if __name__ == "__main__":
	app.run()
