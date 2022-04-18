from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from GoogleNews import GoogleNews
from sqlalchemy.dialects.mysql import LONGTEXT

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)