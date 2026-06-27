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

MAX_ARTICLES = 10
ARTICLES_PER_SOURCE = 5

def fetch_articles():
    articles = []
    seen_urls = set()

    for source in RSS_SOURCES:
        feed = feedparser.parse(source["url"])

        for entry in feed.entries[:ARTICLES_PER_SOURCE]:
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

            if len(articles) >= MAX_ARTICLES:
                return articles

    return articles