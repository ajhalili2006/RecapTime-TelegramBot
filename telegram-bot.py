# Start the imports first.
import os
from dotenv import load_dotenv
import telebot
import logging
import time
import flask

# Set up the directory name and the directories to the .env file first.
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Then setup the environmental variables
Telegram_Token = os.getenv("TOKEN")
Telegram_BotUsername = os.getenv("BOT_USERNAME")

# After settings up, start coding!
bot = telebot.TeleBot(Telegram_Token)

app = flask.Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,"*Howdy, welcome to Recap Time bot!*\n\nTo get started using me, see /quickstart or /help for the full scoop.\n\nTo view your settings", parse_mode="markdown")
  
@bot.message_handler(commands=['support'])
def support_links(message):
  bot.send_message(message, "To access")

bot.polling(print("Logged in as " + Telegram_BotUsername + " on api.telegram.org. If there's error on the bot token, please change it inside .env file."))