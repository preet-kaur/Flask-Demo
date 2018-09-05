from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<user>")  # user logged in or not. Displays default homepage if not logged in (user=None)
def index(user=None):  # by default, user=None, since variable is expected even when not logged in
    return render_template("user.html", user=user)


if __name__ == '__main__':
    app.run()
