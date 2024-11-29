from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Task')


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, SelectField, BooleanField
from wtforms.validators import DataRequired, Optional


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Create Task')


class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete Task')


class ReminderForm(FlaskForm):
    due_date = DateField('Due Date', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Set Reminder')


class RepeatForm(FlaskForm):
    repeat = BooleanField('Repeat Task')
    # Add additional fields as needed for repeat intervals (e.g., daily, weekly, monthly)
    submit = SubmitField('Set Repeat')


class CategoryForm(FlaskForm):
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Set Category')


class TagForm(FlaskForm):
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Add Tag')


class NoteForm(FlaskForm):
    note = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Add Note')


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')