from telegram.ext import ApplicationBuilder, MessageHandler, filters


CHANNEL_B_ID = '@termechaharr'

async def handle_channel_post (update , context):
    tchannel_message = update.channel_post.text
    if "زهرا مهری" in tchannel_message :
        print("پیام شامل کلمه خاص در کانال دریافت شد:", tchannel_message)

    if tchannel_message:

        await context.bot.send_message(chat_id=CHANNEL_B_ID, text=tchannel_message)

app = ApplicationBuilder().token('7905642680:AAEkVWvu1LKoCa0ZrrbZtCtSjBGrRdOWPSo').build()

app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, handle_channel_post))
app.run_polling()


