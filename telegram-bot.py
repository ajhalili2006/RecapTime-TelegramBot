import os
from dotenv import load_dotenv
import telebot

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

Telegram_Token = os.getenv("TOKEN")

bot = telebot.TeleBot(Telegram_Token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, welcome to Recap Time bot!")
  
  
bot.polling(print("Logged in as " + Telegram_Token + " on api.telegram.org"))