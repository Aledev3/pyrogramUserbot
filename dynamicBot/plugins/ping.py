import time

from .. import dynamic
from pyrogram import filters
from pyrogram.types import Message
from ..config import config 

@dynamic.on_message(filters.command("ping", ".") & filters.me)
async def ping(_, msg: Message):
    st = time.time()
    et = time.time()
    mention = msg.from_user.mention
    uptime = f"\n`{round((et - st), 3)} ms`"
    textt = """
★°:･✧*.°☆.*★°●¸★　 
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ┊⍣∙°⚝○｡°✯
┊ ┊ ┊ ┊
┊ ┊ ┊ ⛦『P‌๏‌и‌ɠ‌』 
┊ ┊ ┊︎✫ ˚♡ ⋆˚ ⋆｡ ❀
┊ ┊ ┊
┊ ┊ ┊𓆩𝙈𝙎--≻{} ﮩ٨ـﮩﮩ٨ـ𓆪
┊ ┊ ✯
┊ ✬ ˚•˚✩
┊⍣ •°
┊亗•ʍʏ ๏ωиэя•亗
★• {} •

⚘ Dynamic Bot ⚘
""".format(uptime, mention)
    await msg.edit(textt)
