import feedparser

RSS_URL = "https://hnrss.org/newest?q=AI"
SOURCE_NAME = "Hacker News RSS"

def build_markdown_report(articles):
  lines = []

  lines.append("# AI Trend Daily Report")
  lines.append("")
  lines.append("# 今日のピックアップ")
  lines.append("")

  for index, article in enumerate(articles, start=1):
    lines.append(f"### {index}. {article['title']}")
    lines.append("")
    lines.append(f"- source: {article['source']}")
    lines.append(f"- date; {article['published_at']}")
    lines.append(f"- url: {article['url']}")
    lines.append("")

  return "\n".join(lines)

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

  report = build_markdown_report(articles)
  print(report)


if __name__ == "__main__":
  main()