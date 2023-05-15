from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.String(100))
    date = db.Column(db.String(10))
    time = db.Column(db.String(5))

    def repr(self):
        return f'<task: {self.name}>'

@app.route('/')
def index():
    return render_template('index.html', name = "Jikuttan", sunny = True)

@app.route('/tasks')
def tasks():
    return 'Here is the list of tasks'

@app.route('/tasks/<string:name>')
def task(name):
    return render_template('tasks.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)