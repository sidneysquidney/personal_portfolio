from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from os import environ

from forms import ContactForm

uri = environ.get("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = uri or 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# flask-mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sglethbridge@gmail.com'
app.config['MAIL_PASSWORD'] = 'ioqlewqpqrnquugl'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

sids_variable = 20

class ContactRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), index = True)
    request = db.Column(db.String(1000))

@app.route('/')
def index():
    return render_template('index.html', title='siddhartha lethbridge')

@app.route('/skills')
def skills():
    return render_template('skills.html', title='skills')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='projects')

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            db.session.add(ContactRequest(name = form.name.data, 
                                            email = form.email.data, 
                                            request = form.request.data))
            db.session.commit()
            to_client = Message('Siddhartha Lethbridge - Contact Confirmation', sender = 'sglethbridge@gmail.com', recipients = [form.email.data])
            to_me = Message('Personal Website Inquiry', sender = 'sglethbridge@gmail.com', recipients = ['sglethbridge@gmail.com'])
            to_client.body = f"Dear {form.name.data}. \nThank you for getting in touch. I'll get back to you as soon as I can. \nSiddhartha Lethbridge"
            to_me.body = f"From {form.name.data}, Email: {form.email.data}, Message: {form.request.data}"
            mail.send(to_client)
            mail.send(to_me)
            flash("Form entered successfully. Well done sindey!")
            return redirect(url_for('contact', template_form = form))
    return render_template('contact.html', template_form = form, title='contact')
