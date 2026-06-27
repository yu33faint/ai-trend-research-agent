import feedparser
from datetime import datetime
from config import ARTICLES_PER_SOURCE, MAX_ARTICLES, RSS_SOURCES


def fetch_articles():
    articles = []
    seen_urls = set()

    for source in RSS_SOURCES:
        feed = feedparser.parse(source["url"])

        if feed.bozo:
            print(f"Failed to parse RSS: {source['name']}")
            print(feed.bozo_exception)
            continue

        if not feed.entries:
            print(f"No entries found: {source['name']}")
            continue

        for entry in feed.entries[:ARTICLES_PER_SOURCE]:
            url = entry.get("link", "No URL")

            if url in seen_urls:
                continue

            seen_urls.add(url)

            published_parsed = entry.get("published_parsed")

            if published_parsed:
                published_datetime = datetime(*published_parsed[:6])
            else:
                published_datetime = datetime.min

            article = {
                "title": entry.get("title", "No title"),
                "url": url,
                "source": source["name"],
                "published_datetime": published_datetime,
            }

            articles.append(article)

    articles.sort(key=lambda article: article["published_datetime"], reverse=True)

    return articles[:MAX_ARTICLES]