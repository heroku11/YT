from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developer",url="https://t.me/aryanvikash")],
        [InlineKeyboardButton("Master",url="http://t.me/Xpras_id")],
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton("Report Bug",url="http://t.me/Xpras_id")],
        [InlineKeyboardButton(
            "Or Report Bug", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hallo <b>{message.from_user.first_name}</b>\n/help untuk informasi bantuan lainnya"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
