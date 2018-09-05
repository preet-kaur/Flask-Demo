from flask import Flask, render_template

app = Flask(__name__)


# passing user as variable (username)

@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


# passing other objects, ex: list


@app.route("/shopping")
def shopping():
    food_list = ["Cheese", "Mayonnaise", "Chocolates"]
    return render_template("shopping.html", food_list=food_list)


if __name__ == '__main__':
    app.run()
