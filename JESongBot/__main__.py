# Infinity BOTs <https://t.me/Infinity_BOTs>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm മേരി ചേച്ചി Song Downloader Bot 🎵

Just send me the song name you want to download.
eg: ```/song Faded```

A bot by @MrC_VENOM
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="😎 Developer😎", url="https://t.me/MrC_VENOM"
                    ),
                    InlineKeyboardButton(
                        text="❣ Support Group ❣", url="https://t.me/tvseriezzz"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("marymoody is online.")
idle()
