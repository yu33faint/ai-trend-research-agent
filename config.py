import os


def get_bool_env(name, default):
    value = os.getenv(name)

    if value is None:
        return default

    return value.lower() == "true"


def get_int_env(name, default):
    value = os.getenv(name)

    if value is None:
        return default

    return int(value)


RSS_SOURCES = [
    {
        "name": "Hacker News RSS",
        "url": "https://hnrss.org/newest?q=AI",
    },
    {
        "name": "OpenAI Blog",
        "url": "https://openai.com/blog/rss.xml",
    },
]

MAX_ARTICLES = 10
ARTICLES_PER_SOURCE = 5

ENABLE_AI_SUMMARY = get_bool_env("ENABLE_AI_SUMMARY", False)
AI_PROVIDER = os.getenv("AI_PROVIDER", "dummy")
MAX_AI_SUMMARIES = get_int_env("MAX_AI_SUMMARIES", 1)
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
