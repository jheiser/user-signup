from flask import Flask, request, redirect, render_template, url_for
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', title = "Sign Up")

@app.route("/signup", methods=['POST', 'GET'])
def signup():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "":
        username_error = "Please enter a user name."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters."
        username = ""
    elif " " in username:
        username_error = "Your username cannot contain any spaces."
        username = ""

    if password == "":
        password_error = "Please enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters."
    elif " " in password:
        password_error = "Password cannot contain spaces."
    
    if verify == "" or verify != password:
        verify_error = "Passwords do not match."
        verify = ""

    if email != "":
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)", email):
             email_error = "Not a valid email."
        
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)
    else:
        return render_template(
            'index.html',
            username = username,
            username_error = username_error,
            password_error = password_error,
            verify_error = verify_error,
            email = email,
            email_error = email_error)
    
app.run()