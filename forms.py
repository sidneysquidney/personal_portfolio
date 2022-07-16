from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, TextAreaField, StringField, fields
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms.fields.html5 import EmailField  

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50, min=5, message='Name must be between 5 and 50 characters')])
    email = EmailField('Email', validators=[DataRequired(), Email('Please enter a valid email address'), Length(max=100)])
    request = TextAreaField('Reason For Contact?', validators=[DataRequired(), Length(max=1000, message='Messagee must be under 1000 characters')])
    submit = SubmitField('Submit')