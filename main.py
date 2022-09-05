import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from config import Config

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    bot_name=Config.BOT_NAME,
    force_channel=Config.FORCE_CHANNEL
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
                 InlineKeyboardButton("⚡️𝙐𝙋𝘿𝘼𝙏𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇⚡️", url=f"t.me/{Config.FORCE_CHANNEL}")
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

Send a file (image, video, sticker) under 5 MB
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
⭕ BOT NAME  : SPIDER MAN

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
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
                InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
                ]]
            )
       finally:,
           os.remove(download_path)


@bot.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="image/jetg")
    try:
        link = upload_file(download_path)
        generated_Link = "https://telegra.ph" + "".join(link)
        reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_Link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
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
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


##UPLOAD ANIMATIONS TO THE TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.animation)
async def animation_upload_groups(bot, message):
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
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


## UPLOAD PHOTOS TO TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.photo)
async def photo_upload_groups(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/DevilBotzzSupport>LEARN THIS BOT FIRST!</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


## VIDEO UPLOAD TO THE TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.video)
async def video_upload_group(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/DevilBotzzSupport>LEARN THIS BOT FIRST!</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


## STICKER UPLOAD


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
    except Exception as a:
        await msg.edit_text(
            f"❌ This sticker was unable to upload. Please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>\n\n<i>Caused error - {a}</i>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ]]
        )
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ],[
            InlineKeyboardButton("Web Preview 🔷", url=generated_Link)
            ]]
        )
    finally:
        os.remove(download_path)


## UPLOAD STICKERS TO TELEGRAPH IN GROUPS

@bot.on_message(filters.group & filters.sticker)
async def sticker_upload_group(bot, message):
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
    except Exception as a:
        await msg.edit_text(
            f"❌ This sticker was unable to upload. Please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>\n\n<i>Caused error - {a}</i>",
            reply_markup= InlineKeyboardMarkup( [[
            InlineKeyboardButton("Report Bugs ⚠", url="https://t.me/DevilBotzzSupport")
            ]]
        )
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/DevilBotzzSupport>Feel free to leave a feedback</a>",
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
