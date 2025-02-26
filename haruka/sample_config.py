if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = ""
    OWNER_ID = ""  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = ""

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = ''  # needed for any database modules
    MESSAGE_DUMP = ""  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = "1060318977"  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = "1060318977"  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = "1382148141 1060318977" # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = False
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    STRICT_GBAN = False
    STRICT_GMUTE = False
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = "" # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
