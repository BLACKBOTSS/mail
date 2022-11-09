from pyrogram import Client,filters
from utlis.callback import updateCallback
from utlis.msg import updateHandlers
from utlis.tg import Bot
from config import *
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import threading, requests, time, random,redis
import sched, time ,os
R = redis.Redis(charset="utf-8", decode_responses=True)
app = Client(BOT_ID,
bot_token=TOKEN,
api_id = API_ID,
api_hash = API_HASH
)
@app.on_message(~filters.new_chat_title & ~filters.pinned_message & ~filters.left_chat_member & ~filters.new_chat_photo & ~filters.new_chat_members & ~filters.delete_chat_photo & ~filters.channel)
def update(client, message):
    t = threading.Thread(target=updateHandlers,args=(client, message,R))
    t.daemon = True
    t.start()
@app.on_callback_query()
def callback(client, callback_query ):
    t = threading.Thread(target=updateCallback,args=(client, callback_query,R))
    t.daemon = True
    t.start()
app.run()
