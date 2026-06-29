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

ENABLE_AI_SUMMARY = False
AI_PROVIDER = "dummy"
MAX_AI_SUMMARIES = 1
GEMINI_MODEL = "gemini-3.1-flash-lite"