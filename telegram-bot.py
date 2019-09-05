import os
from dotenv import load_dotenv
import telebot

WEBHOOK_HOST = 'https://garnet-crate.glitch.me'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

Telegram_Token = os.getenv("TOKEN")

bot = telebot.TeleBot(Telegram_Token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "*Howdy, welcome to Recap Time bot!*" + "\n" + "\n" +
              "To")
  
  
bot.polling(print("Logged in as " + Telegram_Token + " on api.telegram.org"))