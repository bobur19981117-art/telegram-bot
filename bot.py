import telebot
import requests
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! TikTok link yubor 👇")

@bot.message_handler(func=lambda message: True)
def download_tiktok(message):
    url = message.text
    
    api = f"https://api.tiklydown.eu.org/api/download?url={url}"
    response = requests.get(api).json()
    
    if response.get("video"):
        video_url = response["video"]["noWatermark"]
        bot.send_video(message.chat.id, video_url)
    else:
        bot.reply_to(message, "Xatolik! Linkni tekshir.")

bot.polling()
