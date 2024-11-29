from flask import Flask, render_template, redirect, url_for, request, flash
from .models import db, User, Task
from .forms import ReminderForm, RepeatForm, CategoryForm, TagForm, NoteForm, SearchForm, TaskForm, DeleteTaskForm
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newtodolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager(app)
# 配置 Flask-Login，例如加载用户回调等
login_manager.login_view = 'login'
login_manager.login_message = "Please log in to access tasks."

db.init_app(app)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username)
        new_user.set_password(password)  # 正确调用 set_password 方法
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()  # 正确的调用方式
        if user and password == user.password:

            login_user(user)  # 登入用户
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            print("invalid")
    return render_template('login.html')


@app.route('/logout')
def logout():
    # 登出逻辑，例如，使用 flask_login 的 logout_user 函数
    logout_user()
    return redirect(url_for('login'))  # 重定向到登录页面


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, static_url='css/style.css')


@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
@app.route('/task/add', methods=['GET', 'POST'])
@login_required
def task_handler(task_id=None):
    task = Task.query.get_or_404(task_id) if task_id else None
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date_str = request.form['due_date']  # 获取日期字符串
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')  # 转换为 datetime 对象
        if task:
            task.title = title
            task.description = description
            task.due_date = due_date
        else:
            new_task = Task(
                title=title,
                description=description,
                due_date=due_date
            )
            db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('task_edit.html', task=task)


# 用户加载器
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 任务管理：用户可以删除任务。
@app.route('/task/<int:task_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    # TODO: 实现删除任务的逻辑
    pass


# 截止日期和提醒：用户可以为任务设置截止日期，并在截止日期前收到提醒。
@app.route('/task/<int:task_id>/set_reminder', methods=['GET', 'POST'])
@login_required
def set_reminder(task_id):
    form = ReminderForm()
    if form.validate_on_submit():
        # TODO: 实现设置提醒的逻辑
        pass
    return render_template('set_reminder.html', form=form)


# 重复任务：应用支持周期性任务的重复设置。
@app.route('/task/<int:task_id>/set_repeat', methods=['GET', 'POST'])
@login_required
def set_repeat(task_id):
    form = RepeatForm()
    if form.validate_on_submit():
        # TODO: 实现设置重复任务的逻辑
        pass
    return render_template('set_repeat.html', form=form)


# 任务分类和标记：用户可以对任务进行分类和标记，便于查找。
@app.route('/task/<int:task_id>/set_category', methods=['GET', 'POST'])
@login_required
def set_category(task_id):
    form = CategoryForm()
    if form.validate_on_submit():
        # TODO: 实现设置任务分类的逻辑
        pass
    return render_template('set_category.html', form=form)


# 标签系统：用户可以为任务添加自定义标签，并能通过标签过滤和搜索任务。
@app.route('/task/<int:task_id>/add_tag', methods=['GET', 'POST'])
@login_required
def add_tag(task_id):
    form = TagForm()
    if form.validate_on_submit():
        # TODO: 实现添加标签的逻辑
        pass
    return render_template('add_tag.html', form=form)


@app.route('/tasks/by_tag/<tag_name>', methods=['GET'])
@login_required
def tasks_by_tag(tag_name):
    # TODO: 实现按标签过滤任务的逻辑
    pass


# 时间线视图：应用包含时间线视图，使用户能够一目了然地查看任务进度。
@app.route('/tasks/timeline', methods=['GET'])
@login_required
def timeline_view():
    # TODO: 实现时间线视图的逻辑
    pass


# 日历视图：开发日历视图，允许用户按日、周或月查看任务和截止日期。
@app.route('/tasks/calendar', methods=['GET'])
@login_required
def calendar_view():
    # TODO: 实现日历视图的逻辑
    pass


# 笔记功能：每个任务附带笔记功能，允许用户为任务添加说明和备忘。
@app.route('/task/<int:task_id>/add_note', methods=['GET', 'POST'])
@login_required
def add_note(task_id):
    form = NoteForm()
    if form.validate_on_submit():
        # TODO: 实现添加笔记的逻辑
        pass
    return render_template('add_note.html', form=form)


# 搜索功能：应用包含搜索功能，使用户能够快速找到所需的笔记。
@app.route('/tasks/search', methods=['GET'])
@login_required
def search_tasks():
    form = SearchForm()
    # TODO: 实现搜索任务的逻辑
    pass
    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)