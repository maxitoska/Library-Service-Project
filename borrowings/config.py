import requests


def telegram_notification_sender(
        some_token: str,
        some_chat_id: str,
        some_message: str
):
    url = f"https://api.telegram.org/bot{some_token}/sendMessage"
    response = requests.get(
        url,
        params={"chat_id": some_chat_id, "text": some_message}
    )
    return response.url
