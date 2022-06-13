import flask
import pynytimes # refer to module https://github.com/michadenheijer/pynytimes
import os
import json

NYTarticles = pynytimes.NYTAPI(os.environ.get('NYTIMES_KEY'),parse_dates=True)

#declaring flask application
app = flask.Flask(__name__)

#on specific path/route, for this app, there's only a single page so i only used "/" as in all pages/path/route
@app.route("/")
def index():
    
    x = 0
    #json.dumps() since the data came as list and json cant load list type of data and change it to str
    starts = json.dumps(NYTarticles.most_viewed(days=1), default=str)
    #loads the json data
    loads = json.loads(starts)
    
    name = "aksa"
    #this will get data from the api and will iterate untill 10 articles/news data recovered
    titles = [loads[x]['title'] for x in range(9)]
    links = [loads[x]['url'] for x in range(9)]
    articles = [loads[x]['abstract'] for x in range(9)]
    photos = [loads[x]['media'][0]['media-metadata'][0]['url'] for x in range(9)] #for this line, we use the url for img tag in the HTML
    return flask.render_template("index.html",name=name,articles=articles, titles=titles, images=photos, links=links )
