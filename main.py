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
                text="πππ ππΌππ ππ πππ½ππΎπππ½π ππ πΎππΌππππ ππ πππ ππππ π½ππ π",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("β‘οΈπππΏπΌππ πΎππΌππππβ‘οΈ", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
Hello π
Nice to meet you π

I am a powerful Telegraph Bot π₯

Hit /help to know my features π
""",
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("DEVELOPER π¨βπ»", url="https://t.me/MR_THOR_01")
            ],[
            InlineKeyboardButton("UPDATES π’", url="https://t.me/DevilBotzz"),
            InlineKeyboardButton("SUPPORT π₯", url="https://t.me/DevilBotzzSupport")
            ]]
            )
        )
            
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
Hello π

/start Check I am Alive

/help To get this message

/about About Me

Send a image under 5 MB size
I can convert that file into Telegraph link π₯

Let's Enjoy π
""",
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("UPDATES π’", url="https://t.me/DevilBotzz"),
            InlineKeyboardButton("SUPPORT π₯", url="https://t.me/DevilBotzzSupport")
            ]]
            )
        )
    
@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
β­ BOT NAME  : Telegraph Bot

β­ CREATOR   : β‘οΈGOD OF THUNDERβ‘οΈ

β­ LANGUAGE  : PYTHON3

β­ FRAMEWORK : PYROGRAM

β­ SERVER    : RAILWAY

β­ COUNTRY   : INDIA
""",
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("SOURCE β€", url="https://github.com/hkcs812/DevilTelegraphBot")
            ],[
            InlineKeyboardButton("UPDATES π’", url="https://t.me/DevilBotzz"),
            InlineKeyboardButton("SUPPORT π₯", url="https://t.me/DevilBotzzSupport")
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
            InlineKeyboardButton("Report Bugs β ", url="https://t.me/DevilBotzzSupport")
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
            InlineKeyboardButton("Report Bugs β ", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview π·", url=generated_Link)
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
            InlineKeyboardButton("Report Bugs β ", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview π·", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


print("I AM ALIVE π₯")

bot.run()
