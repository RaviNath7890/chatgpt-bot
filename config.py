from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "16405341")
API_HASH = getenv("API_HASH", "a84a82371456826203d486f3a0dc7ff3")
BOT_TOKEN = getenv("BOT_TOKEN", "5891981705:AAGzSbhu5BES6uVf0p0EXbVEkTN0V4mO6bU")
OPENAI_API = getenv("OPENAI_API", "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") 
