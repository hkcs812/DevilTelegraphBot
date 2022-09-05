import os


class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_NAME = os.environ.get("BOT_NAME")
    PICS = (environ.get('PICS', 'https://telegra.ph/file/ebe8da68b5d8bfb0f4548.jpg https://telegra.ph/file/a7fbbb10d2f79af0de2b5.jpg https://telegra.ph/file/59dd925676b800f087879.jpg')
    FORCE_CHANNEL = environ.get('FORCE_CHANNEL', '-1001696817546')
