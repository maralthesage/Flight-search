
from telethon import TelegramClient
import telegram

from creds import APP_ID, APP_ID_HASH


# PHONE = "004915730764279"

class NotificationManager:

    # async def send(message):
    #     """
    #     Send a message to a telegram user or group specified on chatId
    #     chat_id must be a number!
    #     """
    #     bot = telegram.Bot(token=TOKEN)
    #     await bot.sendMessage(chat_id="@maralthesage", text=message)

    async def send_telegram(self,message):
        async with TelegramClient('session', APP_ID, APP_ID_HASH) as client:
        # client = TelegramClient('session', APP_ID, APP_ID_HASH)
        #     client.start()
            await client.send_message("@maralthesage",message)
            # client.disconnect()


