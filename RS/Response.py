# -*- coding: utf-8 -*-

import telebot
import libs
from libs import Constant

bot = telebot.TeleBot(Constant.Token)


def Deleter(c_id, m_id):
    try:
        bot.delete_message(c_id, m_id)

    except telebot.apihelper.ApiException:
        pass


def Problem(u_id, lang):
    if Constant.DefaultLang in lang:
        bot.send_message(u_id, 'Ошибка! Не удалось проверить ваш статус Администратора!')

    else:
        bot.send_message(u_id, 'Mistake! Failed to verify your Admin status!')


def ST(u_id, lang):
    if Constant.DefaultLang in lang:
        bot.send_message(u_id, 'Остановка инициализирована')

    else:
        bot.send_message(u_id, 'Stop initialized')


def NCM(title, lang, c_id):
    if Constant.DefaultLang in lang:
        bot.send_message(c_id, f'Добро пожаловать к нам в группу - {title}, будь как дома')

    else:
        bot.send_message(c_id, f'Welcome to our band - {title}, make yourself at home')


def NCT(title, lang, c_id):
    if Constant.DefaultLang in lang:
        bot.send_message(c_id, f'Ух ты! У нас новое название - {title}')

    else:
        bot.send_message(c_id, f'Wow! We have a new name - {title}')


def Dump(c_id, path, name, lang):
    if Constant.DefaultLang in lang:
        bot.send_message(c_id, f'Дамп базы {name} - завершён')
        bot.send_document(c_id, open(path))
    else:
        bot.send_message(c_id, f'Database dump {name} completed')
        bot.send_document(c_id, open(path))


def DumpERR_1(c_id, lang, name):
    if Constant.DefaultLang in lang:
        bot.send_message(c_id, f'Ошибка! База {name} - повреждена или не существует!')
    else:
        bot.send_message(c_id, f'Mistake! Base {name} - corrupt or non-existent!')


def DumpERR_2(c_id, lang):
    if Constant.DefaultLang in lang:
        bot.send_message(c_id, f'Ошибка! Неправильное формирование запроса!')
    else:
        bot.send_message(c_id, f'Mistake! Incorrect formation of the request!')
