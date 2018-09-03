from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is the home page for routing lesson :P'


@app.route('/tuna')
def tuna():
    return '<h2>Cats love Tuna!</h2>'


# Passing Strings in URL
@app.route('/profile/<username>')
def profile(username):
    return "Hello %s" % username


if __name__ == '__main__':
    app.run()
