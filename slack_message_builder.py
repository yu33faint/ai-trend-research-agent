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
    lines.append(f"本日のピックアップ: {len(articles)}件")
    lines.append("")

    if not articles:
        lines.append("本日の重要記事は見つかりませんでした。")
        return "\n".join(lines)

    sections = [
        ("high", "High Priority"),
        ("medium", "Medium Priority"),
    ]

    for importance, section_title in sections:
        section_articles = [
            article for article in articles
            if article.get("importance") == importance
        ]

        if not section_articles:
            continue

        lines.append(f"*{section_title}*")
        lines.append("")

        for index, article in enumerate(section_articles, start=1):
            summary = article.get("summary", "要約は未生成です。")

            if summary == "要約は未生成です。":
                summary = "要約はまだ生成されていません。"

            lines.append(f"*{index}. {article['title']}*")
            lines.append(f"- source: {article['source']}")
            lines.append(f"- category: {article['category']}")
            lines.append(f"- importance: {article['importance']}")
            lines.append(f"- link: <{article['url']}|元記事を開く>")
            lines.append("")
            lines.append("*summary*")
            lines.append(summary)
            lines.append("")

    return "\n".join(lines)