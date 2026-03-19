import requests

WEBHOOK = "ここにDiscordのWebhook URLをそのまま貼る"

requests.post(
    WEBHOOK,
    json={"content": "テスト通知"}
)
