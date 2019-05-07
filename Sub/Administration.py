# -*- coding: utf-8 -*-

import telebot
import libs
import re
import os
import RS.Response as Response
from libs import Constant
from telebot.types import Message
from libs.Constant import MainID

bot = telebot.TeleBot(Constant.Token)


def Dump(message: Message):
    if Constant.COMmode and bot.get_chat_member(MainID, message.from_user.id).status in Constant.Type_Admins:

        if message.chat.type == Constant.Type_Private or message.chat.id == MainID:

            SE = re.search(r'("(\w|\s|\W)*")', message.text)

            if SE:

                SE = re.split(r',', SE.group())

                if '"All"' in SE:

                    for i in Constant.DU_list:

                        Path = f'{os.getcwd()}\\{Constant.DU_list.get(i)}'

                        if os.path.exists(Path):

                            Response.Dump(message.chat.id, Path, i, message.from_user.language_code)

                        else:

                            Response.DumpERR_1(message.chat.id, message.from_user.language_code, i)

                else:

                    for i in SE:

                        SE = re.sub(r'(\s|")', '', i)

                        Path = f'{os.getcwd()}\\{Constant.DU_list.get(SE)}'

                        if SE in Constant.DU_list and os.path.exists(Path):

                            Response.Dump(message.chat.id, Path, SE, message.from_user.language_code)

                        else:

                            Response.DumpERR_1(message.chat.id, message.from_user.language_code, SE)

            else:

                Response.DumpERR_2(message.chat.id, message.from_user.language_code)

        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        Response.Problem(message.from_user.id, message.from_user.language_code)
        Response.Deleter(message.chat.id, message.message_id)

    del message


def ADM(message: Message):
    if Constant.COMmode and bot.get_chat_member(MainID, message.from_user.id).status in Constant.Type_Admins:

        if message.chat.type == Constant.Type_Private or message.chat.id == MainID:

            bot.send_message(message.chat.id, 'Извените, находится в разработке')

        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        Response.Problem(message.from_user.id, message.from_user.language_code)
        Response.Deleter(message.chat.id, message.message_id)

    del message
