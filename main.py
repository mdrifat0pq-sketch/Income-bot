import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# টোকেন গিটহাব থেকে লুকিয়ে সিস্টেম এনভায়রনমেন্ট থেকে নেওয়া হচ্ছে
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("চাইনিজ 🇨🇳", callback_data="lang_zh"),
        InlineKeyboardButton("জাপানিজ 🇯🇵", callback_data="lang_ja"),
        InlineKeyboardButton("কোরিয়ান 🇰🇷", callback_data="lang_ko"),
        InlineKeyboardButton("ইন্দোনেশিয়ান 🇮🇩", callback_data="lang_id")
    )
    bot.send_message(
        message.chat.id, 
        "👋 স্বাগতম! ভিডিওর অরিজিনাল ভাষা সিলেক্ট করুন:", 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def handle_lang(call):
    bot.edit_message_text("🎯 ভাষা সেট করা হয়েছে! এখন আপনার ভিডিওটি পাঠান (সর্বোচ্চ ১০ মিনিট)।", call.message.chat.id, call.message.message_id)

print("বট সচল আছে...")
bot.polling(none_stop=True)
