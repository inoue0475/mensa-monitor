import requests
import os

URL = "https://mensa.jp/exam/"
WEBHOOK = os.environ.get("WEBHOOK_URL")

OPEN_IMAGE = "entry_over.jpg"
FULL_IMAGE = "entry_quota.jpg"

STATE_FILE = "state.txt"

def get_state():
    try:
        with open(STATE_FILE, "r") as f:
            return f.read().strip()
    except:
        return "UNKNOWN"

def save_state(state):
    with open(STATE_FILE, "w") as f:
        f.write(state)

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
    current = check()
    previous = get_state()

    if current == "OPEN" and previous != "OPEN":
        notify("🔥 MENSA募集開始！ https://mensa.jp/exam/")

    save_state(current)
