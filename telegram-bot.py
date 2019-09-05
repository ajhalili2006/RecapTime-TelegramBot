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

bot = telebot.TeleBot(Telegram_Token)

app = flask.Flask(__name__)

WEBHOOK_HOST = 'https://garnet-crate.glitch.me'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (Telegram_Token)
WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "*Howdy, welcome to Recap Time bot!*" + "\n" + 
               "\n" +
              "To")
  
bot.polling(print("Logged in as " + Telegram_Token + " on api.telegram.org"))