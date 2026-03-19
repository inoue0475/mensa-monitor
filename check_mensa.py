import requests

print("START")

WEBHOOK = "https://discord.com/api/webhooks/1484121065134358579/2Xk0eI4G7QS-Zg_5b3xEkf_ergLjx8ESS3l29Mz-lihql9_Sz0RR06vLKw_dQ-xtj0Zc"

response = requests.post(
    WEBHOOK,
    json={"content": "🔥 テスト通知（ログ確認）"}
)

print("STATUS:", response.status_code)
print("END")
