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
    seen_urls = set()

    for source in RSS_SOURCES:
        feed = feedparser.parse(source["url"])

        for entry in feed.entries[:5]:
            url = entry.get("link", "No URL")

            if url in seen_urls:
                continue

            seen_urls.add(url)

            article = {
                "title": entry.get("title", "No title"),
                "url": url,
                "source": source["name"],
                "published_at": entry.get("published", "No published date"),
            }

            articles.append(article)

    return articles