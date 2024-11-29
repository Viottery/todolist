# views.py
from flask import render_template, request, redirect, url_for
from . import app, db
from .models import Task


@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        new_task = Task(title=title, description=description, due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('task_edit.html')
