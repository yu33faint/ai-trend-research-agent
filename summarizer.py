def summarize_article(article):
  # TODO: 将来的にここでOpenAPIなどの生成AI APIを呼び出し，
  # 記事タイトル・出典・公開日・URlをもとに要約文を生成する．
  #
  # 実装イメージ:
  #
  # from openai import OpenAI
  #
  # client = OpenAI()
  #
  # prompt = f"""
  # 以下の記事情報を日本語で短く要約してください。
  #
  # タイトル: {article['title']}
  # 出典: {article['source']}
  # 公開日: {article['published_at']}
  # URL: {article['url']}
  #
  # 出力形式:
  # - 何についての記事か: ...
  # - なぜ重要か: ...
  # - 自分が確認すべき点: ...
  # """
  #
  # response = client.responses.create(
  #     model="gpt-5.5",
  #     input=prompt,
  # )
  #
  # return response.output_text
  return f"{article['title']}に関する要約をここに生成します。"