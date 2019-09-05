import os
from dotenv import load_dotenv
import telebot

WEBHOOK_HOST = 'https://garnet-crate.glitch.me'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)

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
  
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Start flask server
app.run(host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
        debug=True)
  
print("Logged in as " + Telegram_Token + " on api.telegram.org")