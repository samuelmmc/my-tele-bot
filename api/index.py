import os
import telebot
from flask import Flask, request    
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# ကြိုတင်သတ်မှတ်ထားသော အမေး/အဖြေများ
faq_data = {
    "ဈေးဘယ်လောက်လဲ": "ပစ္စည်းတစ်ခုကို ၁၀၀၀၀ ကျပ်ပါ။",
    "လိပ်စာ": "ရန်ကုန်မြို့၊ လှည်းတန်းလမ်းဆုံ အနီးဖြစ်ပါတယ်။",
    "ပို့ဆောင်ခ": "ရန်ကုန်မြို့တွင်း ပို့ဆောင်ခ ၃၀၀၀ ကျပ်ပါ။",
    "ဖုန်းနံပါတ်": "၀၉-၁၂၃၄၅၆၇၈၉ သို့ ဆက်သွယ်နိုင်ပါတယ်။"
}

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    user_text = message.text.strip()
    if user_text in faq_data:
        bot.reply_to(message, faq_data[user_text])
    else:
        default_reply = "တောင်းပန်ပါတယ်။ နားမလည်ပါ။\nအောက်ပါစကားလုံးများကိုသာ မေးပါ -\n- ဈေးဘယ်လောက်လဲ\n- လိပ်စာ"
        bot.reply_to(message, default_reply)

# Vercel URL နှင့် Telegram ကို ချိတ်ဆက်ပေးမည့် လမ်းကြောင်း
@app.route('/setwebhook', methods=['GET'])
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://my-tele-bot-sigma.vercel.app/' + TOKEN)
    return "Webhook Setup Successful!", 200

@app.route('/', methods=['GET'])
def index():
    return "Bot is running on Vercel!"
    
