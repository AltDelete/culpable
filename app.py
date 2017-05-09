import json
import urllib2
import urllib
import requests
import feedparser
import api as AK
from data import get_senate
from flask import Flask, render_template, request

app = Flask(__name__)


key = AK.key
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])

    senate = get_senate()

    return render_template("home.html", articles=feed['entries'], senate=senate['results'][0]['members'])


if __name__ == "__main__":
    app.run(port=5000, debug=True)

    # def get_senate():
    #     url = 'https://api.propublica.org/congress/v1/115/senate/members.json'
    #     request = urllib2.Request(url, headers={"X-API-KEY": key})
    #     data = urllib2.urlopen(request).read()
    #     parsed = json.loads(data)
    #     members = None
    #     if parsed.get("results"):
    #         members = {"first_name": parsed['results'][0]['members']}
    #     return members

    # r = requests.get(url, headers={"X-API-KEY": key})
    # members = json.loads(r.content)
    # return members
