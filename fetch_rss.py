import feedparser
from datetime import date
from pathlib import Path

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

def save_report(report):
  reports_dir = Path("reports")
  reports_dir.mkdir(exist_ok=True)

  today = date.today()
  report_path = reports_dir / f"{today}.md"

  report_path.write_text(report, encoding="utf-8")

  return report_path

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
  report_path = save_report(report)

  print(report)
  print(f"Report saved to: {report_path}")

if __name__ == "__main__":
  main()