from fetch_rss import fetch_articles
from report_builder import build_markdown_report
from report_writer import save_report
from summarizer import summarize_article

def main():
  articles = fetch_articles()

  if articles:
    articles[0]["summary"] = summarize_article(articles[0])

  report = build_markdown_report(articles)
  report_path = save_report(report)

  print(report)
  print(f"Report saved to: {report_path}")

if __name__ == "__main__":
  main()