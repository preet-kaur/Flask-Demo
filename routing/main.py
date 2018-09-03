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


# Passing Integers in URL; need to specify datatype for integers in url
@app.route('/post/<int:post_id>')
def post(post_id):
    return "POST ID is %s" % post_id


if __name__ == '__main__':
    app.run()
