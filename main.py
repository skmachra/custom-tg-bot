from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from threading import Thread
from flask import Flask
import os

# ENV variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Initialize Pyrogram
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Respond to all messages (except the bot's own)
@app.on_message(filters.all & ~filters.me)
async def auto_reply(client, message):
    text = (
        "⚠️ <b>This bot is not working anymore</b> ⚠️\n\n"
        "📢 <b>Please use our new Movies bot 👉 "
        "<a href='https://t.me/SK_Movies1_bot'>@SK_Movies1_bot</a></b>"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Start Bot", url="https://t.me/SK_Movies1_bot")],
        [InlineKeyboardButton("🔄 Updates", url="https://t.me/SK_Movies1")]
    ])

    await message.reply_text(
        text,
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True
    )

# Flask dummy server to keep Koyeb service alive
web = Flask(__name__)

@web.route('/')
def home():
    return "✅ Bot is running!", 200

def run_web():
    web.run(host="0.0.0.0", port=8080)

def run_bot():
    app.run()

# Start both bot and Flask in parallel threads
if __name__ == "__main__":
    Thread(target=run_web).start()
    run_bot()
