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
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

𝐒𝐨𝐮𝐫𝐜𝐞 : [ɢɪᴛʜᴜʙ](https://github.com/AL3X-Github)
𝐌𝐚𝐝𝐞 𝐖𝐢𝐭𝐡 🖤 𝐁𝐲 : [𝐈 𝐙 𝐔 𝐌 𝐈](https://t.me/MaximXRobot)!
    """
