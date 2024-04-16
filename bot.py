from telegram.ext import Updater, CommandHandler

# Обработчик команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот Telegram. Как дела?')

def main():
    # Токен бота, полученный от BotFather
    token = '7081892174:AAGg3j4JqBMNYXI_u1LDG0HcJajOJNh0iT0'
    updater = Updater(token, use_context=True)

    # Получаем объект диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler('start', start))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()