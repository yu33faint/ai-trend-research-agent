from fetch_rss import fetch_articles
from report_builder import build_markdown_report
from report_writer import save_report
from summarizer import summarize_article
from classifier import classify_article, judge_importance
from config import ENABLE_AI_SUMMARY, MAX_AI_SUMMARIES
from article_fetcher import fetch_article_content


def main():
    articles = fetch_articles()

    for article in articles:
        article["category"] = classify_article(article)
        article["importance"] = judge_importance(article)

    if ENABLE_AI_SUMMARY:
        for article in articles[:MAX_AI_SUMMARIES]:
            article["content"] = fetch_article_content(article["url"])
            article["summary"] = summarize_article(article)

    report = build_markdown_report(articles)
    report_path = save_report(report)

    print(report)
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()