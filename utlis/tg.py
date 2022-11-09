import requests
from config import *
import sched, time,datetime,requests
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
def Bot(method,data):
  url = "https://api.telegram.org/bot{}/{}".format(TOKEN,method)
  post = requests.post(url,data=data)
  return post.json()
def run():
  os.system("pm2 restart {}".format(BOT_ID))
def Ckuser(message):
  userID = message.from_user.id
  chatID = message.chat.id
  try:
    response = requests.get('https://tshake.ml/join.php?id={}'.format(userID)).json()
    if response["ok"]:
      return True
    elif response["ok"] == False:
      kb = InlineKeyboardMarkup([[InlineKeyboardButton("اضغط للاشتراك ⏺", url="t.me/zx_xx")] ])
      Bot("sendMessage",{"chat_id":chatID,"text":response["result"],"reply_to_message_id":message.id,"parse_mode":"html","disable_web_page_preview":True,"reply_markup":kb})
      return False
  except Exception as e:
    return True