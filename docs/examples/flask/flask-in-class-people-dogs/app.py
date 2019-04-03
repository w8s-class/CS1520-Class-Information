from flask import (
    Flask, 
    render_template, 
    abort, 
    flash, 
    redirect, 
    url_for,
    request,
    g
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "This is a bad key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///intro.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

person_to_dog_join = db.Table(
    "person_to_dog_join",
    db.Column("person_id", db.Integer(), db.ForeignKey("person.id")),
    db.Column("dog_id", db.Integer(), db.ForeignKey("dog.id")),
)


class Person(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20))
    movie = db.Column(db.String(255))
    dogs = db.relationship(
        "Dog", 
        secondary=person_to_dog_join, 
        backref=db.backref("owners", lazy="select"), 
        lazy="joined"
    )

    def __init__(self, name, movie):
        self.name = name
        self.movie = movie


class Dog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name


people = [
    {
        "name": "Todd",
        "movie": "Harold and Maude",
        "dogs": [
            {"name": "Peppa", "breed": "Golden Doodle"},
            {"name": "Wesley", "breed": "Schnoodle"},
        ],
    },
    {
        "name": "Liz",
        "movie": "The Music Man",
        "dogs": [
            {"name": "Peppa", "breed": "Golden Doodle"},
            {"name": "Wesley", "breed": "Schnoodle"},
        ],
    },
    {
        "name": "Aaron",
        "movie": "Fire Walk with Me",
        "dogs": [{"name": "Arlo", "breed": "Chihuahua"}],
    },
]


@app.route("/")
def hello():
    d = Dog.query.all()

    return render_template("base.html", dogs=d)


@app.route("/<id>/<name>/")
def profile(id, name):
    # flash("This is the profile page!")

    return render_template("profile.html", dog=d)


@app.route("/newDog/")
def add_dog():
    return render_template("add_dog_form.html")


@app.route("/newDog/processForm", methods=["POST"])
def process_dog_form():
    name = request.form.get("dog_name")

    if name is None:
        abort(400)
    
    d = Dog(name)

    db.session.add(d)
    db.session.commit()

    flash("%s IS ALIVE AND NOT DEAD AS PIE" % d.name)

    return redirect(url_for("add_dog"))


@app.cli.command("initdb")
def init_db():
    """Initialize the database"""
    db.drop_all()
    db.create_all()


@app.cli.command("devdata")
def bootstrap_data():
    p = Person("Todd", "Harold and Maude")
    l = Person("Liz", "The Music Man")
    aaron = Person("Aaron", "Fast and the Furious")

    d = Dog("Peppa")
    w = Dog("Wesley")
    arlo = Dog("Arlo")

    arlo.owners.append(aaron)

    p.dogs.append(d)
    p.dogs.append(w)

    d.owners.append(l)
    w.owners.append(l)

    db.session.add(d)
    db.session.add(w)
    db.session.add(p)
    db.session.add(l)
    db.session.add(aaron)
    db.session.add(arlo)
    db.session.commit()


if __name__ == "__main__":
    app.run()
