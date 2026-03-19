import requests
import os

WEBHOOK = os.environ.get("WEBHOOK_URL")

requests.post(
    WEBHOOK,
    json={"content": "🔥 テスト通知（必ず来るはず）"}
)
