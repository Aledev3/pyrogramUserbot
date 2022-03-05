import os
class config(object):
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    PYRO_STRING_SESSION = os.environ.get("PYRO_STRING_SESSION", "")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    BOT_PIC = None 
    TOKEN = os.environ.get("TOKEN", "")
    ALV_TEXT = None
    ALV_PIC = None
    HNDLR = os.environ.get("HNDLR", "\.")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN")
