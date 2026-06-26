import feedparser

RSS_URL = "https://hnrss.org/newest?q=AI"
SOURCE_NAME = "Hacker News RSS"

def main():
  feed = feedparser.parse(RSS_URL)
  articles = []

  for index, entry in enumerate(feed.entries[:5], start=1):
    title = entry.get("title", "No title")
    url = entry.get("link", "No URL")
    published_at = entry.get("published", "No published date")

    article = {
      "title": title,
      "url": url,
      "source": SOURCE_NAME,
      "published_at": published_at,
    }

    articles.append(article)

  for index, article in enumerate(articles, start=1):
    print(f"{index}. {article['title']}")
    print(f"   source: {article['source']}")
    print(f"   date: {article['published_at']}")
    print(f"   url: {article['url']}")
    print()


if __name__ == "__main__":
  main()