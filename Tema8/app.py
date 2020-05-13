from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm
from config import Config

class Form(FlaskForm):
    name = StringField('Name')
    password = PasswordField('Password')
    email = StringField('Email')
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)
    ...
    return render_template("index.html", num_posts=len(posts))

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=Form())

if __name__ == '__main__':
    app.run()