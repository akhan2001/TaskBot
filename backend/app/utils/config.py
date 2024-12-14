import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    SENDER_EMAIL = os.getenv("SENDER")
    RECEIVER_EMAIL = os.getenv("RECEIVER")
    LANGUAGE = os.getenv("LANGUAGE")
