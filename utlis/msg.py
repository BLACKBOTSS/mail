from tg import Bot,Ckuser,run
from config import *
#b
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import threading, requests, time, random, re, json,datetime,os
def updateHandlers(client, message,redis):
	type = message.chat.type
	userID = message.from_user.id
	chatID = message.chat.id
	rank = isrank(redis,userID,chatID)
	text = message.text
	title = message.chat.title
	userFN = message.from_user.first_name
	type = message.chat.type
		if text == "تحديث":
				Bot("sendMessage",{"chat_id":chatID,"text":"تم تحديث الملف","reply_to_message_id":message.id,"parse_mode":"html"})
				run()