import os
from dotenv import load_dotenv


load_dotenv()


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
    {
        "name": "GitHub Blog",
        "url": "https://github.blog/feed/",
    },
    {
        "name": "Google AI Blog",
        "url": "https://blog.google/technology/ai/rss/",
    },
    {
        "name": "AINOW",
        "url": "https://ainow.ai/feed/",
    },
    {
        "name": "Publickey",
        "url": "https://www.publickey1.jp/atom.xml",
    },
    {
        "name": "@IT",
        "url": "https://rss.itmedia.co.jp/rss/2.0/ait.xml",
    },
    {
        "name": "SHIFT AI TIMES",
        "url": "https://shift-ai.co.jp/blog/feed/",
    },
]

MAX_ARTICLES = 10
ARTICLES_PER_SOURCE = 20
MAX_SAFE_AI_SUMMARIES = 1
MAX_ARTICLE_CONTENT_CHARS = get_int_env("MAX_ARTICLE_CONTENT_CHARS", 4000)

HTTP_HEADERS = {
    "User-Agent": "AI-Trend-Research-Agent/0.1"
}

ENABLE_AI_SUMMARY = get_bool_env("ENABLE_AI_SUMMARY", False)
AI_PROVIDER = os.getenv("AI_PROVIDER", "dummy")
MAX_AI_SUMMARIES = min(
    get_int_env("MAX_AI_SUMMARIES", 1),
    MAX_SAFE_AI_SUMMARIES,
)
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")
ENABLE_SLACK_NOTIFY = get_bool_env("ENABLE_SLACK_NOTIFY", False)
MAX_SLACK_ARTICLES = 6

REPORT_HOUR = get_int_env("REPORT_HOUR", 8)
