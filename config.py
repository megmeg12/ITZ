## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCQu06CIbezVp4PyaixyIRPyPg2h83D5QGE2u5OfTS7cAbO_AvGbHAezs30hMG8UcI2ej0g2hIr8U5oI0pPvzcBaOmYOPgOYJ40_QM-t1hlBZNxTWDbrMe9JfXNlyVuhT0MPUhYI3wgjiUjFL4a66msTc9zPlRg3AxoaHm7mNM5lBpDXRBWPpVDFRyzekZMGVEcXRCVhnr2kQxMQ3bvQdYI6vDM5WvU8gQ0_2FGyKuExWoGM2K-PhrRM1ch6vE31szf-x-YpNyoWVNPUeO5liwSckAiI_q8Kl4rqKNOPEAIWdkWQN2xiejCvm-37drEcEcsNa8E9VleY97x-UtCDfHoAAAAAUY1bjQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5527973954:AAGSYoPbUBEZ1neSmbWpk5tb80JnVTcex3I")
BOT_NAME = getenv("BOT_NAME", "PANTERA")
API_ID = int(getenv("API_ID", "19010865"))
API_HASH = getenv("API_HASH", "d53ef9e914d435a305ccc67c204323f2")
OWNER_NAME = getenv("OWNER_NAME", "PANTERA")
OWNER_USERNAME = getenv("OWNER_USERNAME", "musicbotpantera")
ALIVE_NAME = getenv("ALIVE_NAME", "Pantera")
BOT_USERNAME = getenv("BOT_USERNAME", "panteraxmusic_bot")
OWNER_ID = getenv("OWNER_ID", "5472874036")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "panteramusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "THEPANTERAXXX")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "THEPANTERAXXX")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5472874036").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
