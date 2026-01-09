from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "23562992"))
API_HASH = getenv("API_HASH", "e070a310ca3e76ebc044146b9829237c")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", None))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "narzofamily")
UPDATE_CHNL = getenv("UPDATE_CHNL", "narzoxbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@Zolvit")

# Random Start Images
IMG = [
    "https://graph.org/file/1256161197a1c9e5313a0.jpg",
    "https://graph.org/file/1256161197a1c9e5313a0.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
    "CAACAgUAAx0CfLoeOQACKgNmDlwwnocs9yVbS-G5zYz7U9pZKwAC4RAAAkzCcVSCoM-aLK5MsR4E",

]

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
    "🦋",
    "🥀",
    
]
