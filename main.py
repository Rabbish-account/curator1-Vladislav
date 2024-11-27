import telebot

bot = telebot.TeleBot('8136958178:AAFX13bWfPx14L162jIWbvr4m1J5bWw36l0')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Доброе утро!\nВыпей воды\nПомедитируй\nПопотей от физических упражнений',
                     parse_mode='Markdown')

bot.infinity_polling()