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
    if gender.lower() != Gender.male.name and gender.lower() != Gender.female.name:
        return render_template(
            "error.html",
            title="ERROR",
            status=0,
            message="Oops, sorry. Something does not go as we expected.",
        )
    else:
        users = create_several_user(amount=count, gender=gender)
    return render_template("users.html", title=f"{count} user", users=users, status=1)


@app.errorhandler(404)
def error(e):
    return render_template(
        "error.html",
        title="ERROR",
        message="404-page not found",
    )


if __name__ == "__main__":
    app.run(debug=True)
