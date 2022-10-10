import traceback
from data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from StringGenBot.generate import generate_session, ask_ques, buttons_ques


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer("» 𝐓𝐡𝐞 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐖𝐢𝐥𝐥 𝐎𝐧𝐤𝐲 𝐖𝐨𝐫𝐤 𝐈𝐧 𝐓𝐡𝐞 𝐁𝐨𝐭𝐬 𝐖𝐡𝐢𝐜𝐡 𝐀𝐫𝐞 𝐔𝐩𝐠𝐫𝐚𝐝𝐞𝐝 𝐀𝐭 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦!", show_alert=True)
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
            elif query == "pyrogram_bot":
                await callback_query.answer("» 𝐓𝐡𝐞 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐆𝐞𝐧𝐫𝐚𝐭𝐞𝐝 𝐖𝐢𝐥𝐥 𝐁𝐞 𝐎𝐟 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦.", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "𝐖𝐓𝐅! 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐖𝐞𝐧𝐭 𝐖𝐫𝐨𝐧𝐠 \n\n**ᴇʀʀᴏʀ** : {} " \
            "\n\n**𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐨𝐫𝐰𝐚𝐫𝐝 𝐓𝐡𝐢𝐬 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 @MaximXGroup **, 𝐈𝐟 𝐓𝐡𝐢𝐬 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 " \
            "𝐃𝐨𝐞𝐬𝐧'𝐭 𝐂𝐨𝐧𝐭𝐚𝐢𝐧 𝐀𝐧𝐲 𝐒𝐞𝐧𝐬𝐢𝐭𝐢𝐯𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧" \
            "𝐁𝐞𝐜𝐚𝐮𝐬𝐞 𝐓𝐡𝐢𝐬 𝐄𝐫𝐫𝐨𝐫 𝐈𝐬 **𝐍𝐨𝐭 𝐋𝐨𝐠𝐠𝐞𝐝 𝐁𝐲 𝐓𝐡𝐞 𝐁𝐨𝐭** !"
