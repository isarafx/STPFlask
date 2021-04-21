from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    "Create column to store our data"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():

    name = "Son"
    return render_template('home.html', name=name)

@app.route('/about')
def about():
    return "Hello, about page"

@app.route('/script')
def test_script():
    return render_template('test-script.html')

if __name__ == '__main__':
    app.run(debug=True)
