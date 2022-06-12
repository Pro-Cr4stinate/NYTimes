import flask
import pynytimes
import os
import json

NYTarticles = pynytimes.NYTAPI(os.environ.get('NYTIMES_KEY'),parse_dates=True)

app = flask.Flask(__name__)

@app.route("/")
def index():

    x = 0

    starts = json.dumps(NYTarticles.most_viewed(days=1), default=str)
    loads = json.loads(starts)
    name = "aksa"
    titles = [loads[x]['title'] for x in range(9)]
   # link = [loads[x]['url'] for x in range(9)]
    articles = [loads[x]['abstract'] for x in range(9)]
    return flask.render_template("index.html",name=name,articles=articles, titles=titles )