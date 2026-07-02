def build_markdown_report(articles):
    lines = []

    lines.append("# AI Trend Daily Report")
    lines.append("")

    grouped_articles = {
        "high": [],
        "medium": [],
        "low": [],
    }

    for article in articles:
        importance = article.get("importance", "low")

        if importance not in grouped_articles:
            importance = "low"

        grouped_articles[importance].append(article)

    sections = [
        ("high", "High Priority"),
        ("medium", "Medium Priority"),
        ("low", "Low Priority"),
    ]

    for importance, section_title in sections:
        section_articles = grouped_articles[importance]

        if not section_articles:
            continue

        lines.append(f"## {section_title}")
        lines.append("")

        for index, article in enumerate(section_articles, start=1):
            lines.append(f"### {index}. {article['title']}")
            lines.append("")
            lines.append(f"- source: {article['source']}")
            lines.append(f"- category: {article['category']}")
            lines.append(f"- importance: {article['importance']}")
            lines.append(f"- date: {article['published_at']}")
            lines.append(f"- content fetched: {article.get('content_fetched', False)}")
            lines.append(f"- content length: {article.get('content_length', 0)}")
            lines.append(f"- url: [元記事を開く]({article['url']})")
            lines.append("")
            lines.append("#### summary")
            lines.append("")
            lines.append(article["summary"])

    return "\n".join(lines)