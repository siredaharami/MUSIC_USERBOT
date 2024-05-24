from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from PBXMUSIC import app
from PBXMUSIC.utils.database import add_served_chat, delete_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PBXMUSIC.utils.database import get_assistant
import asyncio
from PBXMUSIC.misc import SUDOERS
from PBXMUSIC.mongo.afkdb import HEHE
from PBXMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from PBXMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from PBXMUSIC import app
from PBXMUSIC.utils.bad_ban import admin_filter
from PBXMUSIC.utils.decorators.userbotjoin import UserbotWrapper
from PBXMUSIC.utils.database import get_assistant, is_active_chat

app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/BADMUSIC/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/Badhacker98/PbXbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx 2.0 ᴜ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/PBX_2.0/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/BAD_SPAM_X/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/BADMUSIC/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/Badhacker98/PbXbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx 2.0 ᴜ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/PBX_2.0/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/BAD_SPAM_X/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/BADMUSIC/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/Badhacker98/PbXbot/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx 2.0 ᴜ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/PBX_2.0/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/Badhacker98/BAD_SPAM_X/fork")
                 ]
            ]
        ),
    )
    
# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #



