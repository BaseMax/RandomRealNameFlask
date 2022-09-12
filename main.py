from flask import Flask, render_template
from funcs import *
from Enum import Gender


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("README.html")


@app.route("/get/")
@app.route("/get")
def get_one_user():
    user = create_user()
    return render_template(
        "user.html", title="1 user", user=convert_to_string(user), status=1
    )


@app.route("/get/<int:count>")
def get_several_user(count):
    users = create_several_user(amount=count)
    return render_template("users.html", title=f"{count} user", users=users, status=1)


@app.route("/get/<int:count>/<string:gender>")
def get_user_specific_gender(count, gender):
    types = [Gender.male.name, Gender.female.name, Gender.both.name]
    if gender.lower() in types:
        users = create_several_user(amount=count, gender=gender.lower())
        return render_template(
            "users.html", title=f"{count} user", users=users, status=1
        )
    else:
        return render_template(
            "error.html",
            title="ERROR",
            status=0,
            message="Oops, sorry. Something does not go as we expected.",
        )


@app.route("/get/<string:gender>")
def get_one_user_with_gender(gender):
    types = [Gender.male.name, Gender.female.name, Gender.both.name]
    if gender.lower() in types:
        user = create_user(gender=gender.lower())
        return render_template(
            "user.html", title="1 user", user=convert_to_string(user), status=1
        )
    else:
        return render_template(
            "error.html",
            title="ERROR",
            status=0,
            message="Oops, sorry. Something does not go as we expected.",
        )


@app.errorhandler(404)
def error(e):
    return render_template(
        "error.html",
        title="ERROR",
        message="404-page not found",
    )


if __name__ == "__main__":
    app.run(debug=True)
