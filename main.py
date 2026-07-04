from ai_trend_agent.sources.rss import fetch_articles
from ai_trend_agent.reports.markdown_builder import build_markdown_report
from ai_trend_agent.reports.writer import save_report
from ai_trend_agent.processing.summarizer import summarize_article
from ai_trend_agent.processing.classifier import classify_article, judge_importance
from config import (
    ENABLE_AI_SUMMARY,
    MAX_AI_SUMMARIES,
    ENABLE_SLACK_NOTIFY,
    MAX_SLACK_ARTICLES,
)
from ai_trend_agent.sources.article_fetcher import fetch_article_content
from ai_trend_agent.slack.notifier import send_slack_message
from ai_trend_agent.slack.message_builder import build_slack_message, select_slack_articles
from ai_trend_agent.processing.report_window import get_report_window, is_in_report_window
from ai_trend_agent.reports.source_status import build_source_status
from ai_trend_agent.processing.ai_filter import is_ai_related


def main():
    articles = fetch_articles()

    start, end = get_report_window()

    articles = [
        article for article in articles
        if is_in_report_window(article["published_datetime"], start, end)
    ]

    articles = [
        article for article in articles
        if is_ai_related(article)
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

    source_statuses = build_source_status(articles)
    report = build_markdown_report(articles, source_statuses)
    report_path = save_report(report)

    print(report)
    print(f"Report saved to: {report_path}")

    if ENABLE_SLACK_NOTIFY:
        slack_message = build_slack_message(slack_articles, source_statuses)
        send_slack_message(slack_message)


if __name__ == "__main__":
    main()
