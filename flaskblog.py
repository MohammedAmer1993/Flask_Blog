#!/usr/bin/python3

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "3959627f298c8aa94e73125fc253658862fa1948a8904838c12e7695cad13ef5"
content1 = '''
    this is the content of the frist post
    we hope you enjoy reading it. it is 
    about global warming. thank you very
    much. have a nice day.
'''

content2 = '''
    Egypt is facing alot of injustice. the 
    most terrible thig is you can't talk about
    it or you are tring to remove the regime
    although this regime is worth removing but 
    we are afraid of it
'''
posts = [
    {
        "author": "Mohammed Amer",
        "title": "Golabal warming",
        "date": "20 Mar 2024",
        "content": content1
    },
    {
        "author": "Hossam Bahgat",
        "title": "Free Jouranalism",
        "date": "12 Feb 2024",
        "content": content2
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title="zomrda")


@app.route('/about')
def about():
    return render_template('about.html', title="zomrda")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}', "success")
        return redirect(url_for("home"))
    return render_template("register.html", form=form, title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.email.data == "admin@blog.com" and form.password.data == "amer":
        flash("You are Successfully loged in", "success")
        return redirect(url_for("home"))
    return render_template("login.html", form=form, title="login")


if __name__ == "__main__":
    app.run(debug=True)
