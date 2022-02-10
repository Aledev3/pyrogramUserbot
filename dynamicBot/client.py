from ..config import config
from pyrogram import Client

dynamic = Client(

    session_name=config.STRING_SESSION,

    api_id=config.API_ID,

    api_hash=config.API_HASH,

    plugins={'root': 'dynamic.plugins'}

)



