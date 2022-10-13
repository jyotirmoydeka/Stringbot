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

    START = """ https://te.legra.ph/file/24465e3cbd9767aab29ea.jpg
Hey Bro {}
Welcome To  {} 

If You Don't Trust This Bot 😒, 
❶ Stop Reading This Message 🚫
❷ Delete This Chat Bro 🗑️

🫵 Still Reading!? 
You Can Use Me To Generate Pyrogram New V2 And Telethon String Session. Use Below Buttons To Learn More !

🧑‍💻 By @MaximXRobot 

Source : [Github](https://t.me/+vBu5aXlocTkwNGM1)
Build With ❤️ By : [I𝗓υɱi 和泉](https://t.me/MaximXRobot)
    """
