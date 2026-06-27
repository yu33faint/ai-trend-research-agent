def classify_article(article):
  # 将来はAIで実装予定
  title = article["title"].lower()

  if "agent" in title or "agents" in title:
    return "AIエージェント"
  
  if "model" in title or "llm" in title or "gpt" in title:
    return "AIモデル"
  
  if "github" in title or "developer" in title or "code" in title:
    return "開発ツール"
  
  if "paper" in title or "research" in title or "arxiv" in title:
    return "研究・論文"
  
  if "openai" in title or "google" in title or "microsoft" in title or "nvidia" in title:
    return "企業ニュース"
  
  return "その他"