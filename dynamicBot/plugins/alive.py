import os 
import time
from ..utils import cmd_help
from datetime import datetime
from .. import dynamic, vision, py_v
from pyrogram import filters
from pyrogram.types import Message
from ..config import config  
OWNER_ID = config.OWNER_ID
HNDLR = config.HNDLR 
hl = HNDLR
ALV_PIC = config.ALV_PIC 
ALV_TEXT= config.ALV_TEXT if config.ALV_TEXT else "I AM A FAST PYROGRAM USERBOT WHICH HELPS YOUR ACCOUNT TO MAINTAIN WELL!" 

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += "•".join(time_list)

    return ping_time
    
stime = time.time()
start = datetime.now()
end = datetime.now()
(end - start).microseconds / 1000
uptime = get_readable_time((time.time() - stime))


@dynamic.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, msg: Message): 
      id = msg.from_user.id
      mention = msg.from_user.first_name
      X = f"""
~This is Dynamic UserBot
 ~{ALV_TEXT}~
•ɪɴғᴏ Aʙᴏᴜᴛ Mᴇ•

•Dynamic Vision ~ `{vision}`
•Python Vision ~ `{py_v}`
•My UpTime ~ `{uptime}`
•Security ~ `ON!`
•More About Me ~ [Support Chat](https://Astro_HelpChat)
•My Master ~ [{mention}](tg://user?id={id})

"""
      if ALV_PIC: 
        if ALV_PIC.endswith(".jpg", ".png", ".jpeg"):
           await dynamic.send_photo(msg.chat.id, ALV_PIC, X)
        elif ALV_PIC.endswith(".mp4"):
           await dynamic.send_video(msg.chat.id, ALV_PIC, X)
      else:
          await dynamic.send_message(msg.chat_id, X)


cmd_help("alive", [[".alive", "Check if Bot is Working.."]])
