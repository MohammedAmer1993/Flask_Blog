#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)
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
        "Author": "Mohammed Amer",
        "title": "Golabal warming",
        "date": "20 Mar 2024",
        "content": content1
    },
    {
        "Author": "Hossam Bahgat",
        "title": "Free Jouranalism",
        "date": "12 Feb 2024",
        "content": content2
    }
]


@app.route('/')
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts, title="zomrda")


@app.route('/about')
def mo():
    return render_template('about.html', title="zomrda")


if __name__ == "__main__":
    app.run(debug=True)
