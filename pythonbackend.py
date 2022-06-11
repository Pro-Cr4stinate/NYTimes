import flask
import pynytimes
import os
NYTarticles = pynytimes.NYTAPI("yVgnCb76kweCdxaPGcQcBPNNJo2yU8YH",parse_dates=True)

app = flask.Flask(__name__)

@app.route("/")
def index():
    articles = NYTarticles.most_viewed(days=7)
    name = "aksa"
    return flask.render_template("index.html",name=name,articles=articles )