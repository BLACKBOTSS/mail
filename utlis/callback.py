from tg import Bot
from config import *
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import threading, requests, time, random, re, json,datetime,os
def updateCallback(client, callback_query,redis):
   userID = callback_query.from_user.id
  chatID = callback_query.message.chat.id
  userFN = callback_query.from_user.first_name
  title = callback_query.message.chat.title
  message_id = callback_query.message.id
  date = json.loads(callback_query.data)