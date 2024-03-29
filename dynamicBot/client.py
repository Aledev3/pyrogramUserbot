from dynamicBot.config import config
from pyrogram import Client

dynamic = Client(
    session_name=config.PYRO_STRING_SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins={'root': 'dynamicBot.plugins'}
)

asst = Client(
  "dynamic_bot",
  api_id = config.API_ID,
  api_hash = config.API_HASH,
  bot_token = config.TOKEN,
  plugins={'root': "dynamicBot.assistant"}
)
