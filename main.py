from fetch_rss import fetch_articles
from report_builder import build_markdown_report
from report_writer import save_report

def main():
  articles = fetch_articles()
  report = build_markdown_report(articles)
  report_path = save_report(report)

  print(report)
  print(f"Report saved to: {report_path}")

if __name__ == "__main__":
  main()