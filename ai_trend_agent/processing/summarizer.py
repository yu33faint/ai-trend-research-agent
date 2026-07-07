import os
from google import genai

from config import AI_PROVIDER, GEMINI_MODEL


def build_summary_prompt(article):
    content = article.get("content", "")

    if content:
        content_instruction = "本文を優先し、本文に書かれている内容をもとに要約してください。"
    else:
        content_instruction = "本文は取得できていないため、タイトル・出典・公開日・URLから分かる範囲で、推測しすぎずに整理してください。"

    return f"""
以下の記事情報を、Slackで読みやすい日本語に要約してください。
出力は3行以内にしてください。
推測しすぎず、記事情報から分かる範囲だけを書いてください。

{content_instruction}

タイトル: {article['title']}
出典: {article['source']}
公開日: {article['published_at']}
URL: {article['url']}

本文:
{content}

出力形式:
- 何の記事か:
- なぜ確認する価値があるか:
- 次に見るべき点:
"""


def summarize_article(article):
    if AI_PROVIDER == "dummy":
        return summarize_article_dummy(article)

    if AI_PROVIDER == "gemini":
        return summarize_article_with_gemini(article)

    return "要約プロバイダーが設定されていません。"


def summarize_article_dummy(article):
    return f"{article['title']}に関する要約をここに生成します。"


def summarize_article_with_gemini(article):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Gemini APIキーが設定されていません。"

    prompt = build_summary_prompt(article)

    try:
        client = genai.Client(api_key=api_key)

        interaction = client.interactions.create(
            model=GEMINI_MODEL,
            input=prompt,
        )

        return interaction.output_text

    except Exception as error:
        print(f"Gemini API要約に失敗しました: {article['title']}")
        print(error)
        return "Gemini API要約に失敗しました。"
