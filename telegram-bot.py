# RecapTime-TelegramBot - An repo template to make your own
# Recap Time bot on Telegram.
# Copyright (C) 2019 - Andrei Jiroh
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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

# Then setup the environmental variables. Make sure these are available from .env file.
# Code example:
# CONFIG_VAR-SHPRTCUT_HERE = os.getenv("ENV_VARIABLE_HERE")
Telegram_Token = os.getenv("TOKEN")
Telegram_BotUsername = os.getenv("BOT_USERNAME")

# After we finish on environmental variables, try these first.
bot = telebot.TeleBot(Telegram_Token)
app = flask.Flask(__name__)

# We include some code like these for deep-linking.
def command_extractor(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None

# Now, set up the last part: the commands and others...
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,"*Howdy, welcome to Recap Time bot!*\n\nTo get started using me, see /quickstart or /help for the full scoop.\n\nTo view your settings", parse_mode="markdown")
  
@bot.message_handler(commands=['support, help'])
def support_links(message):
  bot.send_message(message, "To access support page")
  
@bot.message_handler(content_types=['text'])
def command_not_found(message):
	bot.reply_to(message, "Something went wrong on our side. Please try again or see /help for details.\n\nFor more information about *404 Command Not Found*, press the button below or [click here](https://t.me/RecapTime_bot?start=help_404commandnotfound)", parse_mode='markdown')

# When ready, use Polling. If Webhooks, see
bot.polling(print("Logged in as " + Telegram_BotUsername + " on api.telegram.org. If there's error on the bot token, please change it inside .env file."))