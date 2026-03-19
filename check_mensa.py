import requests

URL = "https://mensa.jp/exam/"
WEBHOOK = "https://discord.com/api/webhooks/1484121065134358579/2Xk0eI4G7QS-Zg_5b3xEkf_ergLjx8ESS3l29Mz-lihql9_Sz0RR06vLKw_dQ-xtj0Zc"

OPEN_IMAGE = "entry_over.jpg"
FULL_IMAGE = "entry_quota.jpg"

def check():
    res = requests.get(URL, timeout=10)
    html = res.text

    if OPEN_IMAGE in html:
        return "OPEN"
    if FULL_IMAGE in html:
        return "FULL"
    return "UNKNOWN"

def notify(msg):
    requests.post(WEBHOOK, json={"content": msg})

if __name__ == "__main__":
    status = check()

    if status == "OPEN":
        notify("🔥 MENSA募集開始！ https://mensa.jp/exam/")
