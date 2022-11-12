import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5569794009:AAHLwWzY6-gU20BDjXdIZe7uaG9QXzsgiFs")
      API_ID = int(os.environ.get("APP_ID", 28775362))
      API_HASH = os.environ.get("API_HASH", "773aa8651092039c392a183316fb9e69")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "Join @Ace_ML")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "BOTTOM")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "FlashSpeedster")
