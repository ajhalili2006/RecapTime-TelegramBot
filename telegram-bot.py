# -----START LICENSE INFO-----
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
# -----END LICENSE INFO-----
# -----SUPPORT INFO-----
#
#
#
# -----END SUPPORT INFO----

# Let start boot up the whole program.
print('Booting up...')

# Start the imports first.
print('Starting the import progress...')
import os
from dotenv import load_dotenv
import telebot
from telebot import util
import logging
import time
import flask
print('Imports success!')

# Set up the directory name and the directories to the .env file first.
print("Looking for the .env file...")
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
print("We found the file!")

# Then setup the environmental variables. Make sure its coresponding are available from .env file.
# Code example:
# CONFIG_VAR-SHPRTCUT_HERE = os.getenv("ENV_VARIABLE_HERE")
Telegram_Token = os.getenv("TOKEN")
Telegram_BotUsername = os.getenv("BOT_USERNAME")
print("The bot token is " + Telegram_Token + " and must be running at t.me/" + Telegram_BotUsername + ".")

# We use "tb" instead of "bot before the equal sign"
tb = telebot.TeleBot(Telegram_Token)

tb.polling(none_stop=False, interval=0, timeout=20)
print("Connected to servers! You're now signed in as " + Telegram_BotUsername + ", so we'll now receiving messages.")

# 
updates = tb.get_updates()
print("We got the updates!")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")