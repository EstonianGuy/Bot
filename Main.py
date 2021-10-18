import telebot
from telebot import types

bot = telebot.TeleBot("2098781406:AAFWxCVLjvDhvWzt710APZI_VJWCWLmg_fc", parse_mode=None)
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Эльдар')
# itembtn2 = types.KeyboardButton('v')
# itembtn3 = types.KeyboardButton('d')
markup = types.ReplyKeyboardMarkup()
markup.add(itembtn1)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, welcome on board")
	bot.reply_to(message, 'Хочешь выбрать выбрать сеанс сегодня в кино? Сначала выбери нужный тебе кинотеатр')
	bot.reply_to(message, 'PS бот еще в разработке, поэтому при  появлении проблем или идей обращайтесь	'
						  '                                           '
						  'https://github.com/EstonianGuy/Bot')

@bot.message_handler(func=lambda message: True)
def button_cinema_choice(message):
	chat_id = message.chat.id
	bot.send_message(chat_id,"Hello",reply_markup=markup)


bot.infinity_polling()