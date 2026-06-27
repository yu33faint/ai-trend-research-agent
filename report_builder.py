def build_markdown_report(articles):
    lines = []

    lines.append("# AI Trend Daily Report")
    lines.append("")
    lines.append("## 今日のピックアップ")
    lines.append("")

    for index, article in enumerate(articles, start=1):
        lines.append(f"### {index}. {article['title']}")
        lines.append("")
        lines.append(f"- source: {article['source']}")
        lines.append(f"- date: {article['published_datetime']}")
        lines.append(f"- url: {article['url']}")
        lines.append("")

    return "\n".join(lines)