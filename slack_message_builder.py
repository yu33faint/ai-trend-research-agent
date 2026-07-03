def select_slack_articles(articles, max_count):
    high_articles = [
        article for article in articles
        if article.get("importance") == "high"
    ]

    medium_articles = [
        article for article in articles
        if article.get("importance") == "medium"
    ]

    target_articles = high_articles + medium_articles

    return target_articles[:max_count]


def build_slack_message(articles):
    lines = []

    lines.append("*AI Trend Daily Report*")
    lines.append("")

    if not articles:
        lines.append("本日の重要記事は見つかりませんでした。")
        return "\n".join(lines)

    for index, article in enumerate(articles, start=1):
        lines.append(f"*{index}. {article['title']}*")
        lines.append(f"- source: {article['source']}")
        lines.append(f"- category: {article['category']}")
        lines.append(f"- importance: {article['importance']}")
        lines.append(f"- url: {article['url']}")
        lines.append("")
        lines.append(article["summary"])
        lines.append("")

    return "\n".join(lines)