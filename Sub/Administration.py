# -*- coding: utf-8 -*-

import telebot
import libs
import re
import RS.Response as Response
import Sub.DataBase as DataBase
from libs import Constant
from telebot.types import Message
from libs.Constant import MainID

bot = telebot.TeleBot(Constant.Token)


def GRL(message: Message):
    # Need Data

    if Constant.COMmode and bot.get_chat_member(MainID, message.from_user.id).status in Constant.Type_Admins:

        if message.chat.type == Constant.Type_Private:

            Response.GRL(message.from_user.id, message.from_user.language_code, 'None')

        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        Response.GRP(message.from_user.id, message.from_user.language_code)
        Response.Deleter(message.chat.id, message.message_id)

    del message


def FNL(message: Message):
    # Need Data
    Groups = {}
    Adm = {}

    try:
        SE = re.search(r'(\s"(\w|\s|\W)*")', message.text)
        SE = re.split(r',', SE.group())
    except AttributeError:
        SE == False

    if Constant.COMmode and bot.get_chat_member(MainID, message.from_user.id).status in Constant.Type_Admins:

        if message.chat.type == Constant.Type_Private and SE:

            for SEinfo in SE:

                SEinfo = re.sub(r'(\s|")', '', SEinfo)

                if Groups.get(SEinfo) and Adm.get(SEinfo):

                    SEgroup = f'Name: {SEinfo}\n Id: {Groups.get(str(SEinfo))}'
                    SEadm = f'Name: {SEinfo}\n Id: {Adm.get(str(SEinfo))}'

                    Response.FNL(message.from_user.id, message.from_user.language_code, SEgroup, SEadm)

                else:

                    Response.FNL_1(message.from_user.id, message.from_user.language_code, SEinfo)

        elif not SE and message.chat.type == Constant.Type_Private:

            Response.FNL_2(message.from_user.id, message.from_user.language_code)

        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        Response.GRP(message.from_user.id, message.from_user.language_code)
        Response.Deleter(message.chat.id, message.message_id)

    del message


def ADM(message: Message):
    if Constant.COMmode and bot.get_chat_member(MainID, message.from_user.id).status in Constant.Type_Admins:

        if message.chat.type == Constant.Type_Private:

            bot.send_message(message.chat.id, 'Извените, находится в разработке')

        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        Response.GRP(message.from_user.id, message.from_user.language_code)
        Response.Deleter(message.chat.id, message.message_id)

    del message


def Stop(message: Message):
    if Constant.COMmode and bot.get_chat_member(MainID, message.from_user.id).status in Constant.Type_Creator:

        if message.chat.type in Constant.Type_Private:

            Response.ST(message.from_user.id, message.from_user.language_code)

            return True

        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        Response.GRP(message.from_user.id, message.from_user.language_code)
        Response.Deleter(message.chat.id, message.message_id)

    del message
