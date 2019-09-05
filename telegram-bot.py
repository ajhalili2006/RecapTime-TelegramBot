import os
from dotenv import load_dotenv
import telebot
import logging
import time
import flask

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

Telegram_Token = os.getenv("TOKEN")
Telegram_BotUsername = os.getenv("BOT_USERNAME")

bot = telebot.TeleBot(Telegram_Token)

app = flask.Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,"*Howdy, welcome to Recap Time bot!*\n\nTo get started using me, see /quickstart or /helpfor the full scoop.", parse_mode="markdown")
  
@bot.message_handler(commands=['support'])

  
bot.polling(print("Logged in as " + Telegram_BotUsername + " on api.telegram.org. If there's error on the bot token, please change it inside .env file."))