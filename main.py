import telebot
from telebot.types import Message

#создание бота
bot_client = telebot.TeleBot(token="5485270258:AAGtEaeg4b6KUpF-_gx44ePc-UVH98pViJs")

@bot_client.message_handler(commands=["start"])
def echo(message: Message):
    #print(message.chat.id )
    #print(message.chat.username)
    #с=1
    #от бота мне
    bot_client.send_message(chat_id=message.chat.id,text="Hi, Anatolii Kondratenko from your first telegram bot!")
    #от меня боту
    bot_client.reply_to(message=message, text="Hi, my first telegram bot!")

#запуск бота в режиме pooling
bot_client.polling()
