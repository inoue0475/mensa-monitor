import requests

# ↓ここにDiscordのWebhook URLをそのまま貼る
WEBHOOK = "https://discord.com/api/webhooks/1484121065134358579/2Xk0eI4G7QS-Zg_5b3xEkf_ergLjx8ESS3l29Mz-lihql9_Sz0RR06vLKw_dQ-xtj0Zc"

def notify():
    requests.post(
        WEBHOOK,
        json={"content": "🔥 テスト通知：GitHubから送信成功"}
    )

if __name__ == "__main__":
    notify()
