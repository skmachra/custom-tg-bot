from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Reply on ANY incoming message (except bot's own)
@app.on_message(filters.all & ~filters.me)
async def auto_reply(client, message):
    text = (
        "⚠️ <b>This bot is not working anymore</b> ⚠️\n\n"
        "📢 Please use our new movies bot 👉 <a href='https://t.me/SK_Movies1_bot'>@SK_Movies1_bot</a>"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Start Bot", url="https://t.me/SK_Movies1_bot")],
        [InlineKeyboardButton("🔄 Updates", url="https://t.me/SK_Movies1")]
    ])

    await message.reply_text(text, reply_markup=keyboard, parse_mode="html", disable_web_page_preview=True)

app.run()
