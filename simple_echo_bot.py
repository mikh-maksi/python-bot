from telegram.ext import Application, MessageHandler, CommandHandler, filters

TOKEN = "7516686821:AAHTbg4UmGGBgQVIdNN1zUYqam2t0ia43JE"

async def start(update, context):
    string_out = "Привіт! Я ... бот. Вгадай слово, пов'язане із опитуванням"
    await update.message.reply_text(string_out)

async def reply_hello(update, context):
    string_in = update.message.text
    print(string_in)
    if (string_in == "quiz"):
        string_out = "Зараз стартуємо опитування"
    else:
        string_out = "Не вгадав!"
    await update.message.reply_text(string_out)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT, reply_hello))

app.run_polling()

# pip install python-telegram-bot