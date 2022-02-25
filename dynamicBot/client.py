from ..config import config
from pyrogram import Client

dynamic = Client(
    session_name=config.PYRO_STRING_SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins={'root': 'dynamicBot.plugins'}
)

assnt = Client(
  api_id = config.API_ID,
  api_hash = config.API_HASH
  bot_token = config.TOKEN
  plugins= dict("dynamicBot.plugins.asst")
)
