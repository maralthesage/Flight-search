from telegram.ext._updater import Updater
from telegram._update import Update
from telegram.ext._callbackcontext import CallbackContext
from telegram.ext._commandhandler import CommandHandler
from telegram.ext._messagehandler import MessageHandler
from telegram.ext.filters import UpdateFilter
from flight_search import FlightSearch
import asyncio
from creds import TOKEN


# class TelegramBot():
updater = Updater(TOKEN, update_queue=asyncio.Queue)
flight_search = FlightSearch()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Enter the city you want to fly from.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("Your Message")


def get_flight_code( update: Update, context: CallbackContext):
    update.message.reply_text(f"you city_code is {flight_search.get_destination_code(update.message)}")

# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('get_flight_code', get_flight_code))
updater.start_polling()


