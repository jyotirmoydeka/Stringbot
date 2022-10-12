from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, Random
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo=
                [
"https://te.legra.ph/file/0325da0c1422acc1ee7a3.jpg",
"https://te.legra.ph/file/a9f0df8afe53e8b8154a5.jpg",
"https://te.legra.ph/file/7cf3fcf1778acc3184997.jpg",
"https://te.legra.ph/file/b7322de19b8c94d3fc6f3.jpg",
"https://te.legra.ph/file/95e7dc37f427a0a2e5e64.jpg",
"https://te.legra.ph/file/c1a5426d0e0fc8e893c99.jpg",
"https://te.legra.ph/file/24465e3cbd9767aab29ea.jpg",
"https://te.legra.ph/file/d9e3166c983d690d378c5.jpg",
"https://te.legra.ph/file/67864aa1f1a1a79714a0f.jpg",
"https://te.legra.ph/file/17dd53b6a5922431bf01e.jpg",
"https://te.legra.ph/file/cb101461c47f25f088ed3.jpg",
"https://te.legra.ph/file/2e0a00b2545ba2e8ff0cd.jpg",
"https://te.legra.ph/file/86037156a878c0273df07.jpg",
"https://te.legra.ph/file/1bcbec5bd64dd502afff2.jpg",
"https://te.legra.ph/file/ed3d3b5fc1cdb6626c4a5.jpg",
"https://te.legra.ph/file/19a6b6842a5e0e8a510e1.jpg",
"https://te.legra.ph/file/af3f9a03186608f0d56cf.jpg",
"https://te.legra.ph/file/3fd1351cbd218e1047773.jpg",
"https://te.legra.ph/file/d3827183fdecbe0bf313f.jpg",
"https://te.legra.ph/file/77e4388f1d68a6557755f.jpg",
"https://te.legra.ph/file/f83b2a809d9424ffc6485.jpg",
"https://te.legra.ph/file/230ee12a06cd0f42bbe63.jpg",
"https://te.legra.ph/file/230ee12a06cd0f42bbe63.jpg"
] caption=f"➤ According To My Database You've Not Joined [Group/Channel]({link}) Yet, If You Want To Use Me Then Join [Group/Channel]({link}) And Start Me Again 😉",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Maxim X Bots", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
