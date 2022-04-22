from dynamicBot.client import dynamic, assnt
from pyrogram.errors import AccessTokenInvalid, ApiIdInvalid, ApiIdPublishedFlood


if __name__ == "__main__":
    try:
        assnt.start()  # Not using run as wanna print 
        dynamic.run() # using run for session client
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your TOKEN is not valid.")
