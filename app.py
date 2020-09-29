import telebot
import json
from telebot import types
from classes.player import *
from classes.world import *

with open('config.json', 'r', encoding='utf-8') as fh: 
    data = json.load(fh)

bot = telebot.TeleBot(data['TOKEN'])

@bot.message_handler(commands=['start'])  
def helpp(message):
    bot.send_message(message.chat.id, "Зарагистрируйся путник \n\n /reg_name твое_имя")

@bot.message_handler(commands=['reg_name'])
def reg(message):
    if len(message.text) > 10:
        reg_player_name = message.text.split(' ')
        for i in World.players:
            if i.id == message.chat.id:
                bot.send_message(message.chat.id, 'Ты уже зарегестрирован друг !')
                return 0
        World.add_player(Player(message.chat.id, reg_player_name[1], ''))
        bot.send_message(message.chat.id, 'Введи свой класс ! (Герой, Маг) \n\n /reg_class выбранный класс')

@bot.message_handler(commands=['reg_class'])
def reg_class(message):
    if len(message.text) > 11:
        if message.text.split(' ')[1].lower() == 'герой' or message.text.split(' ')[1].lower() == 'маг':
            for i in World.players:
                if i.id == message.chat.id:
                    if i._class != '':
                        bot.send_message(message.chat.id, 'Ты уже зарегестрирован друг !')
                        return 0
            if message.text.split(' ')[1].lower() == 'маг': World.players[0] = Mag(World.players[0])
            elif message.text.split(' ')[1].lower() == 'герой': World.players[0] = Hero(World.players[0])
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton("/menu")
            markup.add(item1)
            bot.send_message(message.chat.id, 'Ты успешно попал в мир ! друг мой', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Такого класса не существует !')

@bot.message_handler(commands=['info'])
def info(message):
    for i in World.players:
        if i.id == message.chat.id:
            bot.send_message(message.chat.id, f'Имя: {i.name}\nКласс: {i._class}\nЗдоровье: {i.helf}\nСила: {i.power}\nОружие: {i.weapon.name}\n {message.chat.id} ')

@bot.message_handler(commands=['menu'])
def menu(message):
    player = World.return_player(message.chat.id)
    if player._class == 'Маг':
                if player.weapon.name == 'magick stick':
                    bot.send_message(message.chat.id, player.name)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton("Мои характеристики", callback_data='info')
                    item2 = types.InlineKeyboardButton("Рюкзак", callback_data='backpack')
                    markup.add(item1, item2)
                    bot.send_message(message.chat.id, f'{"❤" * player.helf}                 {player._class}')
                    bot.send_photo(message.chat.id, 'https://ibb.co/WsdTpHN', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'info':
                i = World.return_player(call.message.chat.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton("/close")
                markup.add(item1)
                bot.send_message(call.message.chat.id, f'Имя: {i.name}\nКласс: {i._class}\nЗдоровье: {i.helf}\nСила: {i.power}\nОружие: {i.weapon.name}', reply_markup=markup)
            elif call.data == 'backpack':
                bot.send_message(call.message.chat.id, 'noting')
    except Exception as e:
        print(repr(e))

@bot.message_handler(commands=['close'])
def close(message): pass


bot.polling(none_stop=True)
