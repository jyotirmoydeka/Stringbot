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
Hey Bro {}
Welcome To  {} 

If You Don't Trust This Bot 😒, 
❶ Stop Reading This Message 🚫
❷ Delete This Chat Bro 🗑️

🫵 Still Reading!? 
You Can Use Me To Generate Pyrogram New V2 And Telethon String Session. Use Below Buttons To Learn More !

❏ 𝐌𝐚𝐱𝐢𝐦 𝐗 𝐁𝐨𝐭𝐬
┣ ☁️ Source Code : [Click Here](https://t.me/+vBu5aXlocTkwNGM1)
┣ 🔥 Framework : [Pyrogram](https://docs.pyrogram.org)
┗ 🗣️ Language : [Python](https://www.python.org)

❏ 🧑‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 ━┓
┗ @MaximXRobot
    """
