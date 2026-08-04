import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك 🌹\nأنا بوت جاهز للخدمة."
    )


# ترحيب بالأعضاء الجدد
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await update.message.reply_text(
            f"🌹 أهلاً وسهلاً {user.first_name} نورت المجموعة."
        )


# الردود التلقائية
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # اسم مستخدم البوت
    bot_username = (await context.bot.get_me()).username.lower()

    if "السلام عليكم" in text:
        await update.message.reply_text("عليكم السلام 🌚💜")

    elif "مرحباً" in text or "مرحبا" in text:
        await update.message.reply_text("مراحب 🌹")

    elif "ايدي صبيحاوي" in text:
        await update.message.reply_text("5507893736")

    elif "مساء الخير" in text:
        await update.message.reply_text("مساء النور 🌹")

    elif "شلونكم شباب" in text:
        await update.message.reply_text("الحمد لله بخير دامك بخير 💜")

    # الرد عند منشن البوت
    elif f"@{bot_username}" in text and "احبج" in text:
        await update.message.reply_text("يعمري واني هم احبك 🌚💜")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
)
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
)

print("Bot is running...")
app.run_polling()