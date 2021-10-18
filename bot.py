import requests, emoji, os, random
import pandas as pd

# This is commented because it's not used for GitHub Actions
# from env import TOKEN, CHAT

# Uncomment this instead if you want to run this locally
TOKEN, CHAT = os.environ['TOKEN'], os.environ['CHAT']

# https://www.webfx.com/tools/emoji-cheat-sheet/
def send(bot_message):
    resp = requests.get(emoji.emojize(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT}&parse_mode=Markdown&text={bot_message}&disable_web_page_preview=true", use_aliases = True))
    return resp.json()

"""
with open('truths.txt', 'r') as f:
    verses = f.readlines()
    i = random.randint(1, (len(verses)+1)//3) - 1
    send(f"*{verses[3*i].strip()}*\n{verses[3*i+1].strip()}")
"""

data = pd.read_csv("truths.csv", encoding="ISO-8859-1", names=["text", "ref"])
i = random.randint(1, data.shape[0]) - 1
print("Send output:",send(f"{data.loc[i, 'text']}\n*  - {data.loc[i, 'ref']}*")["ok"])