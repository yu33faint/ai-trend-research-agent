AI_KEYWORDS = [
    "ai",
    "artificial intelligence",
    "生成ai",
    "人工知能",
    "llm",
    "gpt",
    "chatgpt",
    "gemini",
    "claude",
    "copilot",
    "agent",
    "agents",
    "aiエージェント",
    "機械学習",
    "machine learning",
    "deep learning",
]

AI_RELATED_SOURCES = [
    "OpenAI Blog",
    "Google AI Blog",
    "AINOW",
]


def is_ai_related(article):
    if article["source"] in AI_RELATED_SOURCES:
        return True

    title = article["title"].lower()

    return any(keyword in title for keyword in AI_KEYWORDS)