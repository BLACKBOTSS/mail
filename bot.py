from config import *
from pyrogram import Client,filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import threading, requests, time, random
import redis
import sched, time ,os
R = redis.Redis(charset="utf-8", decode_responses=True)
app = Client(BOT_ID,
bot_token=TOKEN,
api_id = API_ID,
api_hash = API_HASH
)
def Bot(method,data):
  url = "https://api.telegram.org/bot{}/{}".format(TOKEN,method)
  post = requests.post(url,data=data)
  return post.json()
  def run():
  os.system("pm2 restart {}".format(BOT_ID))
  def updateHandlers(client, message,redis):
  	type = message.chat.type
  userID = message.from_user.id
  chatID = message.chat.id
  text = message.text
  title = message.chat.title
  if text == "تحديث":
  	Bot("sendMessage",{"chat_id":chatID,"text":"تم تحديث الملف","reply_to_message_id":message.id,"parse_mode":"html"})
  run()
  @app.on_message(~filters.new_chat_title & ~filters.pinned_message & ~filters.left_chat_member & ~filters.new_chat_photo & ~filters.new_chat_members & ~filters.delete_chat_photo & ~filters.channel)
  def update(client, message):
  	t = threading.Thread(target=updateHandlers,args=(client, message,R))
  t.daemon = True
  t.start()
  app.run()