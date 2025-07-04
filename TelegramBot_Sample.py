from telegram.ext import ApplicationBuilder, MessageHandler, filters


CHANNEL_B_ID = '@TELEGRAM CHANNEL ADDRESS'

async def handle_channel_post (update , context):
    tchannel_message = update.channel_post.text
    if "SPECIFIC FORMAT" in tchannel_message :
        print("THE MESSAGE WAS RECEIVED IN A SPECIFIC FORMAT : ", tchannel_message)

    if tchannel_message:

        await context.bot.send_message(chat_id=CHANNEL_B_ID, text=tchannel_message)

app = ApplicationBuilder().token('TOKEN : ').build()

app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, handle_channel_post))
app.run_polling()


