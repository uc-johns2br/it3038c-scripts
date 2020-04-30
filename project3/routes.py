from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def hello():
    #name = 'AJ'
    return render_template("index.html")

@app.route("/search", methods=['POST'])
def search():
    return render_template("search.html", TwitterName=request.form['TwitterName'])

