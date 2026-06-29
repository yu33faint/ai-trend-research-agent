from config import AI_PROVIDER


def summarize_article(article):
    if AI_PROVIDER == "dummy":
        return summarize_article_dummy(article)

    if AI_PROVIDER == "gemini":
        return summarize_article_with_gemini(article)

    return "要約プロバイダーが設定されていません。"


def summarize_article_dummy(article):
    return f"{article['title']}に関する要約をここに生成します。"


def summarize_article_with_gemini(article):
    # TODO: 将来的にここでGemini APIを呼び出す。
    # 無料枠で安全に使うため，まずは最新一件のみを対象にする。
    # APIキーは環境変数GEMINI_API_KEYから読み込む予定。
    return "Gemini API要約は未実装です。"
