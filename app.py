from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/articles/<article>")
def article(article=None):
    return render_template("articles/{}.html".format(article))
