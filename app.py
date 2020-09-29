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
            bot.send_message(message.chat.id, 'Ты успешно попал в мир ! друг мой')
        else:
            bot.send_message(message.chat.id, 'Такого класса не существует !')

@bot.message_handler(commands=['info'])
def info(message):
    for i in World.players:
        if i.id == message.chat.id:
            bot.send_message(message.chat.id, f'Имя: {i.name}\nКласс: {i._class}\nЗдоровье: {i.helf}\nСила: {i.power}\nОружие: {i.weapon.name}\n {message.chat.id} ')

@bot.message_handler(commands=['iii'])
def test(message):
    for i in World.players:
        if i.id == int(message.text.split(' ')[1]):
            bot.send_message(message.chat.id, i.name)


bot.polling(none_stop=True)
