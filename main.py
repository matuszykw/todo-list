from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    
@app.route('/')
def home():
    tasks = Todo.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('task-name')
    add_task = Todo(task=name, done=False)
    db.session.add(add_task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:task_id>')
def update(task_id):
    task = Todo.query.get(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Todo.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)