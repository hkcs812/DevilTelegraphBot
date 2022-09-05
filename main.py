import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from telegraph import upload_file
from config import Config

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

PICS = [
 "https://telegra.ph/file/09b2cb624771a83dd4983.jpg",
 "https://telegra.ph/file/a720f26abeb6bd9adc05b.jpg",
 "https://telegra.ph/file/c1769c1b965f74dc733a5.jpg",
 "https://telegra.ph/file/edfe00b950eea33361d25.jpg",
 "https://telegra.ph/file/2005d7e440130620378fa.jpg",
 "https://telegra.ph/file/843ca93b7b817ca42aaab.jpg",
 "https://telegra.ph/file/a1e27dcbb467ad610aa0e.jpg",
 "https://telegra.ph/file/c19b77e8644312a50b32c.jpg",
 "https://telegra.ph/file/db4da737589be75593629.jpg",
 "https://telegra.ph/file/edb27ed98b9c9275db431.jpg",
]

force_channel = "DevilBotzz"



@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await message.reply_text(
                text="𝙔𝙊𝙐 𝙃𝘼𝙑𝙀 𝙏𝙊 𝙎𝙐𝘽𝙎𝘾𝙍𝙄𝘽𝙀 𝙈𝙔 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝙏𝙊 𝙐𝙎𝙀 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 😁",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("⚡️𝙐𝙋𝘿𝘼𝙏𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇⚡️", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
Hello 👋
Nice to meet you 🙌

I am a powerful Telegraph Bot 🔥

Hit /help to know my features 😍
""",
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("DEVELOPER 👨‍💻", url="https://t.me/MR_THOR_01")
            ],[
            InlineKeyboardButton("UPDATES 📢", url="https://t.me/DevilBotzz"),
            InlineKeyboardButton("SUPPORT 👥", url="https://t.me/DevilBotzzSupport")
            ]]
            )
        )
            
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
Hello 👋

/start Check I am Alive

/help To get this message

/about About Me

Send a image under 5 MB size
I can convert that file into Telegraph link 🔥

Let's Enjoy 🎉
""",
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("UPDATES 📢", url="https://t.me/DevilBotzz"),
            InlineKeyboardButton("SUPPORT 👥", url="https://t.me/DevilBotzzSupport")
            ]]
            )
        )
    
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
⭕ BOT NAME  : Telegraph Bot

⭕ CREATOR   : ⚡️GOD OF THUNDER⚡️

⭕ LANGUAGE  : PYTHON3

⭕ FRAMEWORK : PYROGRAM

⭕ SERVER    : RAILWAY

⭕ COUNTRY   : INDIA
""",
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("SOURCE ❤", url="https://github.com/hkcs812/DevilTelegraphBot")
            ],[
            InlineKeyboardButton("UPDATES 📢", url="https://t.me/DevilBotzz"),
            InlineKeyboardButton("SUPPORT 👥", url="https://t.me/DevilBotzzSupport")
            ]]
            )
        )
    
@bot.on_message(filters.photo & filters.private)
async def photo_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(
        message=message, file_name="image/jetg"
    )
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ]]
        )
    finally:
        os.remove(download_path)


@bot.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)

        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


@bot.on_message(filters.sticker)
async def sticker_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


print("I AM ALIVE 🔥")

bot.run()
