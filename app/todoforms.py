from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Task')