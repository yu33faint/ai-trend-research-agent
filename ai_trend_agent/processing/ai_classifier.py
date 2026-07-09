import json
import os
from google import genai

from config import AI_PROVIDER, GEMINI_MODEL, AI_CLASSIFICATION_CHUNK_SIZE
from ai_trend_agent.processing.classifier import classify_article, judge_importance

VALID_CATEGORIES = {
    "AIエージェント",
    "AIモデル",
    "開発ツール",
    "研究・論文",
    "企業ニュース",
    "その他",
}
VALID_IMPORTANCE = {"high", "medium", "low"}

def build_classification_prompt(articles):
    lines = []
    for index, article in enumerate(articles):
        lines.append(
            f"{index}: title=\"{article['title']}\" "
            f"source=\"{article['source']}\" "
        )
    article_text = "\n".join(lines)

    return f"""
以下は本日収集したAI関連記事の一覧です。各記事について、
category (AIエージェント / AIモデル / 開発ツール / 研究・論文 / 企業ニュース / その他) と importance (high / medium / low) を判定して下さい。

出力は必ず次のJSON配列形式のみで、説明文はつけないでください。
[
    {{"index": 0, "category": "AIモデル", "importance": "high"}},
    ...
]

記事一覧:
{article_text}
"""


def classify_articles_with_gemini(articles):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    prompt = build_classification_prompt(articles)

    try:
        client = genai.Client(api_key=api_key)

        interaction = client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt,
        )

        results = json.loads(interaction.output_text)
        parsed = {}

        for result in results:
            index = result.get("index")
            category = result.get("category")
            importance = result.get("importance")

            if category in VALID_CATEGORIES and importance in VALID_IMPORTANCE:
                parsed[index] = (category, importance)

        return parsed

    except Exception as error:
        print("Gemini分類に失敗しました。ルールベースにフォールバックします。")
        print(error)
        return None


def classify_articles(articles):
    if AI_PROVIDER != "gemini":
        _classify_with_rules(articles)
        return

    for start in range(0, len(articles), AI_CLASSIFICATION_CHUNK_SIZE):
        chunk = articles[start:start + AI_CLASSIFICATION_CHUNK_SIZE]
        parsed = classify_articles_with_gemini(chunk)

        for offset, article in enumerate(chunk):
            if parsed is not None and offset in parsed:
                article["category"], article["importance"] = parsed[offset]
            else:
                article["category"] = classify_article(article)
                article["importance"] = judge_importance(article)


def _classify_with_rules(articles):
    for article in articles:
        article["category"] = classify_article(article)
        article["importance"] = judge_importance(article)