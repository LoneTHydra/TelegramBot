# -*- coding: utf-8 -*-

import telebot
import libs
from libs import Constant
from libs.Constant import MainID

bot = telebot.TeleBot(Constant.Token)


def Deleter(c_id, m_id):
    try:
        bot.delete_message(c_id, m_id)

    except telebot.apihelper.ApiException:
        pass


def GRL(u_id, lang, Data):
    if Constant.DefaultLang in lang:
        bot.send_message(u_id, f'Вот что известно мне:\n$Name, ID, Administrator$\n{Data} ')
        # bot.send_message(u_id, f'Список известных мне групп:\n{Groups}')
        # bot.send_message(u_id, f'Список известных мне администраторов:\n{Adm}')
        pass

    else:
        bot.send_message(u_id, f"Here's what I know:\n$Name, ID, Administrator$\n{Data} ")
        # bot.send_message(u_id, f'A list of all known groups:\n{Groups}')
        # bot.send_message(u_id, f'A list of all known administrators:\n{Adm}')


def GRP(u_id, lang):
    if Constant.DefaultLang in lang:
        bot.send_message(u_id, 'Ошибка! (Не удалось проверить ваш статус)')

    else:
        bot.send_message(u_id, 'Mistake! (Unable to verify your status)')


def FNL(u_id, lang, SEgroup, SEadm):
    if Constant.DefaultLang in lang:
        bot.send_message(u_id, f'Вот известная мне информация:\n\
    	$О самой группе:\n{SEgroup}\n\
    	$О её администраторах:\n{SEadm}')

    else:
        bot.send_message(u_id, f'Here is known me information:\n\
    		$About the group:\n{SEgroup}\n\
    		$About its administrators:\n{SEadm}')


def FNL_1(u_id, lang, title):
    if Constant.DefaultLang in lang:
        bot.send_message(u_id, f'Группы с именем ({title}) не найдено. Возможно вы допустили ошибку в вводе!')

    else:
        bot.send_message(u_id, f'No group with name ({title}) found. Perhaps you made a mistake in the input!')


def FNL_2(u_id, lang):
    if Constant.DefaultLang in lang:
        bot.send_message(u_id, 'Ошибка! (Формирование запроса)')

    else:
        bot.send_message(u_id, 'Mistake! (Forming a request)')


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
        bot.send_message(c_id, f'Хах! Нас назвали по другому - {title}')

    else:
        bot.send_message(c_id, f'Huh! We were named differently - {title}')


def NCP(title, lang, c_id):
    print('i am NCP')
    # What is this???
