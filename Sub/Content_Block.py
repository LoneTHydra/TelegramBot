# -*- coding: utf-8 -*-

import telebot
import libs
import RS.Response as Response
from libs import Constant
from telebot.types import Message

bot = telebot.TeleBot(Constant.Token)


def Text(message: Message):
    if message.chat.type in Constant.Type_Groups:

        if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Admins or Constant.Text:

            if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Restricted:

                Response.Deleter(message.chat.id, message.message_id)

            else:

                pass
        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        pass

    del message


def AVNV(message: Message):
    if message.chat.type in Constant.Type_Groups:

        if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Admins or Constant.AVNV:

            if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Restricted:

                Response.Deleter(message.chat.id, message.message_id)

            else:

                pass
        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        pass

    del message


def Doc(message: Message):
    if message.chat.type in Constant.Type_Groups:

        if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Admins or Constant.Doc:

            if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Restricted:

                Response.Deleter(message.chat.id, message.message_id)

            else:

                pass
        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        pass

    del message


def Photo(message: Message):
    if message.chat.type in Constant.Type_Groups:

        if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Admins or Constant.Photo:

            if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Restricted:

                Response.Deleter(message.chat.id, message.message_id)

            else:

                pass
        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        pass

    del message


def Sticker(message: Message):
    if message.chat.type in Constant.Type_Groups:

        if bot.get_chat_member(message.chat.id,
                               message.from_user.id).status in Constant.Type_Admins or Constant.Sticker:

            if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Restricted:

                Response.Deleter(message.chat.id, message.message_id)

            else:

                pass
        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        pass

    del message


def LC(message: Message):
    if message.chat.type in Constant.Type_Groups:

        if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Admins or Constant.LC:

            if bot.get_chat_member(message.chat.id, message.from_user.id).status in Constant.Type_Restricted:

                Response.Deleter(message.chat.id, message.message_id)

            else:

                pass
        else:

            Response.Deleter(message.chat.id, message.message_id)

    else:

        pass

    del message


def NCM(message: Message):
    if message.chat.type in Constant.Type_Groups and Constant.NCM:

        # Response.Deleter(message.chat.id, message.message_id)
        # It Need?

        Response.NCM(message.chat.title, message.from_user.language_code, message.chat.id)

    else:

        pass

    del message


def LCM(message: Message):
    if message.chat.type in Constant.Type_Groups and not Constant.LCM:

        Response.Deleter(message.chat.id, message.message_id)

    else:
        pass

    del message


def NCT(message: Message):
    if message.chat.type in Constant.Type_Groups and Constant.NCT:

        Response.NCT(message.chat.title, message.from_user.language_code, message.chat.id)

    # Response.Deleter(message.chat.id, message.message_id)
    # Is need?

    else:

        pass

    del message


def NCP(message: Message):
    if message.chat.type in Constant.Type_Groups and Constant.NCP:

        # Response.NCP(message.chat.title, message.from_user.language_code, message.chat.id)
        pass

    # Response.Deleter(message.chat.id, message.message_id)
    # Is need?

    else:

        pass

    del message
