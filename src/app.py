from flask import Flask
from urllib.request import urlopen
import json


app = Flask(__name__)


def curl(url):
    page = urlopen(url)
    data_bytes = page.read()
    return data_bytes.decode("utf-8")


@app.route("/")
def index():
    return (
        "Welcome to ScratchDBUpgraded. You can find documentation on the forum thread."
    )


"""

@app.route("/test")
def test():
    return f"Welcome to the testing page"


@app.route("/test/<thing>")
def test2(thing):
    return f"Welcome to the testing page: {thing}"
"""


@app.route("/v1/news/raw")
def v1_news_raw():
    return curl("https://api.scratch.mit.edu/news")


@app.route("/v1/news/<key>/id")
def v1_news_id(key):
    news = curl("https://api.scratch.mit.edu/news")
    parseable = json.loads(news)
    return str(parseable[int(key)]["id"])
