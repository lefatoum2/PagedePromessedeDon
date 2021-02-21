from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from pymongo import MongoClient
import os
from Flask_WTforms.model import RegForm
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# from passlib.hash import sha256_crypt
from functools import wraps
from Version2.model import *

app = Flask(__name__)

# Connection au cluster
app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017")
db = client.ORE

# Connection à la collection
collection1 = db.dons


# Page d'acceuil
@app.route("/")
@app.route("/accueil")
def accueil():
    return render_template('accueil.html')


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
def dons():
    res = collection1.find()
    return render_template('dons.html', res=res)


# Enregistrement Utilisateur
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        """
        password = sha256_crypt.encrypt(str(form.password.data))

         # Create cursor
        cur = mysql.connection.cursor()

        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
                    (name, email, username, password))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)
"""


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']


"""
        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')
"""


# Vérification si toujours connecté
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))

    return wrap


# Déconnection
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
