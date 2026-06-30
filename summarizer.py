import os
from dotenv import load_dotenv

from config import AI_PROVIDER


load_dotenv()

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
    # TODO: 将来的にここでGemini APIを呼び出す。
    # 実装時はgoogle-gemini SDKを使う。
    #
    # from google import genai
    #
    # client = genai.Client()
    #
    # prompt = f"""
    # 以下の記事情報を日本語で短く要約してください。
    #
    # タイトル: {article['title']}
    # 出典: {article['source']}
    # 公開日; {article['published_at']}
    # URL: {article['url']}
    # """
    #
    # response = client.interactions.create(
    #     model=GEMINI_MODEL,
    #     input=prompt,
    # )
    #
    # return response.output_text

    return "Gemini API要約は未実装です。"
