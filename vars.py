#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24179222"))
API_HASH = environ.get("API_HASH", "a92e863ced5b205cc9e52be34b3e9e35")
BOT_TOKEN = environ.get("BOT_TOKEN", "8323473706:AAE8OU9hKcXPKaSYpJy-A-ljvdIDwgIWiUI")

OWNER = int(environ.get("OWNER", "5647194983"))
CREDIT = environ.get("CREDIT", "𝑀ཞ ᭄Ꭺຮ𝖍υ⁰⁷࿐")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5647194983').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5647194983').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set




