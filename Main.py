# -*- coding: utf-8 -*-

import telebot
import libs
import Sub
import time
from libs import Constant
from telebot.types import Message
from Sub import Administration
from Sub import Content_Block

bot = telebot.TeleBot(Constant.Token)

Service = False


@bot.message_handler(commands=['Dump'])
def Ad_1(message: Message):
    Administration.Dump(message)


# @bot.message_handler(commands=['Find'])
# def Ad_2(message: Message):
#    Administration.FNL(message)


@bot.message_handler(commands=['Menu'])
def Ad_3(message: Message):
    Administration.ADM(message)


@bot.message_handler(commands=['Stop'])
def Ad_4(message: Message):
    global Service
    Service = Administration.Stop(message)
    if Service:
        bot.stop_bot()


@bot.message_handler(content_types=['text'])
def text(message: Message):
    Content_Block.Text(message)


@bot.message_handler(content_types=['audio', 'vidio', 'vidio_note', 'voice'])
def avnv(message: Message):
    Content_Block.AVNV(message)


@bot.message_handler(content_types=['document'])
def doc(message: Message):
    Content_Block.Doc(message)


@bot.message_handler(content_types=['photo'])
def photo(message: Message):
    Content_Block.Photo(message)


@bot.message_handler(content_types=['sticker'])
def sticker(message: Message):
    Content_Block.Sticker(message)


@bot.message_handler(content_types=['location', 'contact'])
def lc(message: Message):
    Content_Block.LC(message)


@bot.message_handler(content_types=['new_chat_members'])
def ncm(message: Message):
    Content_Block.NCM(message)


@bot.message_handler(content_types=['left_chat_member'])
def lcm(message: Message):
    Content_Block.LCM(message)


@bot.message_handler(content_types=['new_chat_title'])
def nct(message: Message):
    Content_Block.NCT(message)


while not Service:
    try:
        bot.polling(none_stop=True, timeout=60)
    except Exception as Err:
        print(Err)
        time.sleep(2)
