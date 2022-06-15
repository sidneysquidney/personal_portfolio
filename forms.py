from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, fields
from wtforms.validators import DataRequired, Email, Length, ValidationError #EmailField

# from flask.ext.wtf import Form
# from wtforms import validators
# from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='yoyou fill in'), Length(max=50, min=5, message='less than 50 please')])
    email = StringField('Email', validators=[DataRequired(), Email('Please enter your email address you moron'), Length(max=100)])
    # email = EmailField('Email', validators=[DataRequired(), Email('Please enter your email address you moron'), Length(max=100)])
    request = TextAreaField('Reason For Contact?', validators=[DataRequired('fill in this field dummy'), Length(max=1000)])
    submit = SubmitField('Submit')