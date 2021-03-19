from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner", url="https://t.me/featzai")],
        [InlineKeyboardButton(
            "Url Uploader", url="https://t.me/Ftz4i")]
    ])
    welcomed = f"Namaste <b>{message.from_user.first_name} We are made for goodness 😌🍉 </b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
