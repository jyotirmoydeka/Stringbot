from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐒𝐞𝐬𝐬𝐢𝐨𝐧", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭️", url="https://t.me/MaximXGroup"),
         InlineKeyboardButton("𝐌𝐚𝐬𝐭𝐞𝐫", url="https://t.me/MaximXRobot"),
        ],
    ]

    START = """
Hey Bruh {} 😉,

This Is I𝗓υɱi 和泉 {} ⚡,
I Can Generate Pyrogram And Telethon String Session, Use The Below Button And Go Ahead!
Written in Python With the Help of Pyrogram.

Source : [Github](https://t.me/+vBu5aXlocTkwNGM1)
Build With ❤️ By : [I𝗓υɱi 和泉](https://t.me/MaximXRobot)
    """
