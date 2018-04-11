import telebot
from telebot import types

#import constants, os, re

#smilecode
insta = '\U0001F4F7'
utub = '\U0001F3A5'
vklogo = '\U0001F171'
lik = '\U0001F44D'
disl = '\U0001F44E'

token = '476836709:AAGX-faqpExRbjuJsD3JK-4ltO963Eeyaow'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Новости", 
callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="Админы", 
callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="Задать вопрос", 
callback_data="NumberTree")
    but_4 = types.InlineKeyboardButton(text="Обо мне", 
callback_data="Number4")
    key.add(but_1, but_2, but_3, but_4)
    msg = bot.send_message(message.chat.id, "Главное меню", reply_markup=key)

def aboutmenu(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Инстаграмм " + insta, url="https://www.instagram.com/maxspace_star/")
    but_2 = types.InlineKeyboardButton(text="Вконтакте " + vklogo, url="https://vk.com/max_f_s_f" )
    but_3 = types.InlineKeyboardButton(text="Ютуб " + utub, url="https://www.youtube.com/channel/UCpJeVeHasI04hxRU_u-FxmA?view_as=subscriber")
    but_4 = types.InlineKeyboardButton(text=lik, callback_data="Like")
    but_5 = types.InlineKeyboardButton(text=disl, callback_data="dislike")
    key.add(but_1, but_2, but_3, but_4, but_5)
    msg = bot.send_message(message.chat.id, "Видеовизитка https://youtu.be/SZlGj72uJcI", reply_markup=key)
    
@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'NumberOne':
        msg = bot.send_message(c.message.chat.id, 'Это кнопка 1')
    if c.data == 'NumberTwo':
        msg = bot.send_message(c.message.chat.id, 'Это кнопка 2')
    if c.data == 'NumberTree':
        msg = bot.send_message(c.message.chat.id, 'Это кнопка 3')
    if c.data == 'Number4':
        aboutmenu(c.message)
    if c.data == 'Like':
        msg = bot.send_message(c.message.chat.id, 'Вам понравилось')
    if c.data == 'dislike':
        msg = bot.send_message(c.message.chat.id, 'Вам не понравилось')
if __name__ == '__main__':
     bot.polling(none_stop=True)
