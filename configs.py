import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "22350063"))
  API_HASH = os.environ.get("API_HASH", "21306fd66006fd927c22bbe0af42943c")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7617535781:AAEXIIAX5dOWAFEFMvarnt0kRqN0Vp-kvRw")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "kratosXmania_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002156849345","7135258368"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "https://diskwala.com/")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "6773ea07d87f1f5f7ab21a54")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7135258368"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://nbolt4500:<db_password>@cluster0.cv9r7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002184025553")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002354196816","-1002222075129"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
