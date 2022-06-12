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
    titles = loads[0]['title']
    urls = loads[0]['url']
    articles = loads[0]['abstract']
    photos = loads[x]['media'][0]['media-metadata'][0]['url']
    return flask.render_template("index.html",articles=articles, titles=titles, link=urls, images=photos)
