import requests


def telegram_notification_sender(
        token: str,
        chat_id: str,
        message: str
):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    response = requests.get(
        url,
        params={"chat_id": chat_id, "text": message}
    )
    return response.url
