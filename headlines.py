import feedparser
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

RSSFEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'dailymail': 'https://www.dailymail.co.uk/articles.rss',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640',
            'infowars': 'https://www.infowars.com/feed/custom_feed_rss'}


@app.route("/")
def getNews():
    query = request.args.get('publication')
    if not query or query.lower() not in RSSFEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
    feed = feedparser.parse(RSSFEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)
