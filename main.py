from fetch_rss import fetch_articles
from report_builder import build_markdown_report
from report_writer import save_report
from summarizer import summarize_article
from classifier import classify_article, judge_importance
from config import (
    ENABLE_AI_SUMMARY,
    MAX_AI_SUMMARIES,
    ENABLE_SLACK_NOTIFY,
    MAX_SLACK_ARTICLES,
)
from article_fetcher import fetch_article_content
from ai_trend_agent.slack.notifier import send_slack_message
from ai_trend_agent.slack.message_builder import build_slack_message, select_slack_articles
from report_window import get_report_window, is_in_report_window


def main():
    articles = fetch_articles()

    start, end = get_report_window()

    articles = [
        article for article in articles
        if is_in_report_window(article["published_datetime"], start, end)
    ]

    for article in articles:
        article["category"] = classify_article(article)
        article["importance"] = judge_importance(article)

    slack_articles = select_slack_articles(articles, MAX_SLACK_ARTICLES)

    if ENABLE_AI_SUMMARY:
        for article in slack_articles[:MAX_AI_SUMMARIES]:
            content = fetch_article_content(article["url"])

            article["content"] = content
            article["content_fetched"] = bool(content)
            article["content_length"] = len(content)
            article["summary"] = summarize_article(article)

    report = build_markdown_report(articles)
    report_path = save_report(report)

    print(report)
    print(f"Report saved to: {report_path}")

    if ENABLE_SLACK_NOTIFY:
        slack_message = build_slack_message(slack_articles)
        send_slack_message(slack_message)


if __name__ == "__main__":
    main()
