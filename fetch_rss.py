import feedparser

RSS_SOURCES = [
    {
        "name": "Hacker News RSS",
        "url": "https://hnrss.org/newest?q=AI",
    },
    {
        "name": "OpenAI Blog",
        "url": "https://openai.com/blog/rss.xml",
    },
]

def fetch_articles():
    articles = []

    for source in RSS_SOURCES:
        feed = feedparser.parse(source["url"])

        for entry in feed.entries[:5]:
            article = {
                "title": entry.get("title", "No title"),
                "url": entry.get("link", "No URL"),
                "source": source["name"],
                "published_at": entry.get("published", "No published date"),
            }

            articles.append(article)

    return articles