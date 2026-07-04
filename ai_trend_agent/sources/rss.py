import feedparser
from datetime import datetime, timezone
from config import ARTICLES_PER_SOURCE, RSS_SOURCES
from ai_trend_agent.sources.url_cleaner import clean_url


def fetch_articles():
    articles = []
    seen_urls = set()
    fetch_statuses = []

    for source in RSS_SOURCES:
        feed = feedparser.parse(source["url"])

        if feed.bozo:
            error_message = str(feed.bozo_exception)

            print(f"Failed to parse RSS: {source['name']}")
            print(error_message)

            fetch_statuses.append({
                "source": source["name"],
                "status": "failed",
                "error": error_message,
            })

            continue

        if not feed.entries:
            print(f"No entries found: {source['name']}")

            fetch_statuses.append({
                "source": source["name"],
                "status": "empty",
                "error": "",
            })

            continue
        
        fetch_statuses.append({
            "source": source["name"],
            "status": "ok",
            "error": "",
        })

        for entry in feed.entries[:ARTICLES_PER_SOURCE]:
            url = entry.get("link", "No URL")
            url = clean_url(url)

            if url in seen_urls:
                continue

            seen_urls.add(url)

            published_parsed = entry.get("published_parsed")

            if published_parsed:
                published_datetime = datetime(*published_parsed[:6], tzinfo=timezone.utc)
            else:
                published_datetime = datetime.min

            article = {
                "title": entry.get("title", "No title"),
                "url": url,
                "source": source["name"],
                "published_at": entry.get("published", "No published date"),
                "published_datetime": published_datetime,
                "summary": "要約は未生成です。",
            }

            articles.append(article)

    articles.sort(key=lambda article: article["published_datetime"], reverse=True)

    return articles, fetch_statuses