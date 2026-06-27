import feedparser

RSS_URL = "https://hnrss.org/newest?q=AI"
SOURCE_NAME = "Hacker News RSS"


def fetch_articles():
    feed = feedparser.parse(RSS_URL)
    articles = []

    for entry in feed.entries[:5]:
        article = {
            "title": entry.get("title", "No title"),
            "url": entry.get("link", "No URL"),
            "source": SOURCE_NAME,
            "published_at": entry.get("published", "No published date"),
        }

        articles.append(article)

    return articles