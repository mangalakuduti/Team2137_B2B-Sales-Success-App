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

@app.route('/', methods=['POST', 'GET'])
def index():
   if request.method == 'POST':
       company = request.form['content']
       googlenews.search(company)
       results = googlenews.results()
       res = []
       for result in results:
           temp = []
           temp.append("TITLE: " + result["title"])
           temp.append("DESC: " + result["desc"])
           temp.append("URL: " + result["link"])
           res.append('\n'.join(temp))
       res.insert(0,company.upper())
       body = '\n\n'.join(res)
       new_task = Todo(content=body)
       googlenews.clear()
       try:
           db.session.add(new_task)
           db.session.commit()
           return redirect('/')
       except:
           return 'There was an issue adding your task'
   else:
       tasks = Todo.query.order_by(Todo.date_created).all()
       return render_template('index.html', tasks=tasks)
 
 
@app.route('/delete/<int:id>')
def delete(id):
   task_to_delete = Todo.query.get_or_404(id)
 
   try:
       db.session.delete(task_to_delete)
       db.session.commit()
       return redirect('/')
   except:
       return 'There was a problem deleting that task'


if __name__ == "__main__":
    app.run(debug=True)
