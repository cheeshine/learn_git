from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<username>')
def user(username):
    return render_template('user.html', name=username)
if __name__ == '__main__':
    app.run(debug=True)
