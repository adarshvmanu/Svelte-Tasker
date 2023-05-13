from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.String(100))

    def repr(self):
        return f'<task: {self.name}>'

@app.route('/')

def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)