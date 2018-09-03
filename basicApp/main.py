from flask import Flask

app = Flask(__name__)  # app is Flask object __name__: help determine root path


@app.route('/')
def index():
    return 'This is the homepage'


if __name__ == "__main__":  # makes sure that app.run(..) is executed only when this file is called directly
    app.run(debug=True)   #Start this app/web server
    #Run app only if it is main file

    #Done!
