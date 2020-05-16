from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm
from config import Config
import psycopg2

class Form(FlaskForm):
    name = StringField('Name')
    password = PasswordField('Password')
    email = StringField('Email')
    submit = SubmitField('Submit')

def AddDBEntry(nam, ema, pas):
    conn=psycopg2.connect("host=hagrid.delhelsa.com user=python password=greencore dbname=py09")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO webform VALUES (%s, %s, %s)",(nam, ema, pas))
    conn.commit()
    conn.close()

def CountEntries():
    conn=psycopg2.connect("host=hagrid.delhelsa.com user=python password=greencore dbname=py09")
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM webform")
    count=cursor.fetchone()
    conn.close()
    return count[0]



app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)

    return render_template("index.html", num_count=CountEntries())

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        AddDBEntry(name, email, password)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup_form.html", form=Form())

if __name__ == '__main__':
    app.run()

