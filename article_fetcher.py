import requests
from bs4 import BeautifulSoup


def fetch_article_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines()]
        clean_lines = [line for line in lines if line]

        content = "\n".join(clean_lines)

        return content[:4000]

    except Exception as error:
        print(f"記事本文の取得に失敗しました: {url}")
        print(error)
        return ""