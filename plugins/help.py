from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Hanya bisa digunakan untuk 1 video (Bukan Untuk Playlist video) Pastikan untuk menyertakan url / link youtube video"
    await message.reply_text(helptxt)
