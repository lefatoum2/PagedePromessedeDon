from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from pymongo import MongoClient
import os
from Flask_WTforms.model import RegForm
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from Version2.model import *
import bcrypt

app = Flask(__name__)

# Connection au cluster
app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017")
db = client.ORE

# Connection à la collection des dons et des utilisateurs
collection1 = db.dons
records = db.users


# Page d'acceuil
@app.route("/")
@app.route("/accueil")
def accueil():
    return render_template('accueil.html')


# Vérification si toujours connecté
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'email' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap


# Formulaire
@app.route("/form", methods=['GET', 'POST'])
def formulaire():
    form = DonForm(request.form)
    if request.method == 'POST' and form.validate():
        name_first = form.name_first.data
        name_last = form.name_last.data
        email = form.email.data
        money = form.money.data
        checkbox = form.checkbox.data

        collection1.insert(
            {"name": name_first, "name_last": name_last, "email": email, "money": money, "checkbox": checkbox})

        flash('Thank You', 'success')

        return redirect(url_for('accueil'))

    return render_template('formulaire.html', form=form)


# Affichage des dons

@app.route("/dons")
@is_logged_in
def dons():
    res = collection1.find()
    return render_template('dons.html', res=res)


# Enregistrement Utilisateur
@app.route('/register', methods=['GET', 'POST'])
def register():

    if "email" in session:
        return redirect(url_for("dons"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")

        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('register.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('register.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('register.html', message=message)
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'name': user, 'email': email, 'password': hashed}
            records.insert_one(user_input)

            user_data = records.find_one({"email": email})
            new_email = user_data['email']

            return render_template('login.html', email=new_email)
    return render_template('register.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("dons"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']

            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('dons'))
            else:
                if "email" in session:
                    return redirect(url_for("dons"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)


# Déconnection
@app.route('/logout')
@is_logged_in
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("accueil.html")
    else:
        return render_template('accueil.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
