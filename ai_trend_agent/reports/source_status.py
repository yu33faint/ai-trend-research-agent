from config import RSS_SOURCES


def count_articles_by_source(articles, source_name):
    return len([
        article for article in articles
        if article["source"] == source_name
    ])

def build_source_status(
    fetched_articles,
    window_articles,
    ai_articles,
    slack_articles,
):
    source_statuses = []

    for source in RSS_SOURCES:
        source_name = source["name"]

        fetched_count = count_articles_by_source(fetched_articles, source_name)
        window_count = count_articles_by_source(window_articles, source_name)
        ai_count = count_articles_by_source(ai_articles, source_name)
        slack_count = count_articles_by_source(slack_articles, source_name)

        source_statuses.append({
            "source": source_name,
            "fetched_count": fetched_count,
            "window_count": window_count,
            "ai_count": ai_count,
            "slack_count": slack_count,
        })

    return source_statuses