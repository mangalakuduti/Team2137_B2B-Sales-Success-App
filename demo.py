from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from GoogleNews import GoogleNews
from sqlalchemy.dialects.mysql import LONGTEXT

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
googlenews = GoogleNews(lang='en', period='`5d')
 
class Todo(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.String, nullable=False)
   date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)
