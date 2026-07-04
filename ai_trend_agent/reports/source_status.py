from config import RSS_SOURCES


def build_source_status(articles):
    source_statuses = []

    for source in RSS_SOURCES:
        source_name = source["name"]

        source_articles = [
            article for article in articles
            if article["source"] == source_name
        ]

        source_statuses.append({
            "source": source_name,
            "count": len(source_articles),
            "has_articles": len(source_articles) > 0
        })

    return source_statuses