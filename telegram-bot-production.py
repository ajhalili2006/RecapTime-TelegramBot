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
import dotenv
from dotenv import load_dotenv
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
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

# After we finish on environmental variables, do these business:
bot = telebot.TeleBot(Telegram_Token)
app = flask.Flask(__name__)

# We include some code like these for deep-linking.
# ---START IMPORTS HERE---
# TODO: Please help me make code for deep links!
# ---AND END HERE---

# Now, set up the last part: the commands and others... So, let's start the commands first.
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message,"*Howdy, welcome to Recap Time bot!*\n\nTo get started using me, see /quickstart or /help for the full scoop.\n\nTo view your settings", parse_mode="markdown")
  
@bot.message_handler(commands=['quickstart'])
def
    
# For other messages that the bot can't process, we use the fallback message for that case.
@bot.message_handler(content_types=['text'])
def command_not_found(message):
	bot.reply_to(message, "Something went wrong on our side. Please try again or see /help for details.\n\nFor more information about *404 Command Not Found*, press the button below or [click here](https://t.me/RecapTime_bot?start=help_404commandnotfound)", parse_mode='markdown');print("An user tired to " +
  "sent an command or message but neither the server or the bot itself doesn't understand it.")

# Speaking of Inline mode, we use some code samples from
@bot.inline_handler(lambda query: query.query == 'samples_github-repo:eternnoir/pyTelegramBotAPI')
def query_text(inline_query):
    try:
        media_samples = types.InlineQueryResultPhoto('3',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
                                         )
        media_samples2 = types.InlineQueryResultPhoto('4',
                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg')
        media_samples3 = types.InlineQueryResultVideo('5',
                                         'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
                                         'video/mp4', 'Video',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                                         'Title'
                                         )
        bot.answer_inline_query(inline_query.id, [media_samples, media_samples2], media_samples3)
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: len(query.query) is 0)
def default_query(inline_query):
    try:
        default = types.InlineQueryResultArticle('1', 'For help in using my inline search, click me.', types.InputTextMessageContent("To get started using me, you can try the following keywords to search around the bot." +
        "\n" + "\n" + "To see this help message again, just type `@RecapTime_bot` then space.", parse_mode="markdown"))
        articlesearch = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, [default])
    except Exception as e:
        print(e)
# We're
# When ready, use Polling. If Webhooks, see docs for info.
print("The whole Python code is in good state, as what the Python test results said. We're connecting to Telegram servers...")
bot.polling(print("Logged in as " + Telegram_BotUsername + " on api.telegram.org. Everything will gone right, unless you update your code and do the wrong things. Congrats!"))