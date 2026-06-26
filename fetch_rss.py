import feedparser

RSS_URL = "https://hnrss.org/newest?q=AI"
SOURCE_NAME = "Hacker News RSS"

def main():
  feed = feedparser.parse(RSS_URL)

  for index, entry in enumerate(feed.entries[:5], start=1):
    title = entry.get("title", "No title")
    url = entry.get("link", "No URL")
    published_at = entry.get("published", "No published date")

    print(f"{index}. {title}")
    print(f"  source: {SOURCE_NAME}")
    print(f"  date: {published_at}")
    print(f"  url: {url}")
    print()


if __name__ == "__main__":
  main()