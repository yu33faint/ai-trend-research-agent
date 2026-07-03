import requests

from config import SLACK_WEBHOOK_URL


def send_slack_message(text):
    if not SLACK_WEBHOOK_URL:
        print("Slack Webhook URLが設定されていません。")
        return False

    payload = {
        "text": text,
    }

    try:
        response = requests.post(
            SLACK_WEBHOOK_URL,
            json=payload,
            timeout=10,
        )
        response.raise_for_status()

        print("Slackに通知しました。")
        return True

    except Exception as error:
        print("Slack通知に失敗しました。")
        print(error)
        return False
