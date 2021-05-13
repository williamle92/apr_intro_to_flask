from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired, EqualTo, Email




class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField()
