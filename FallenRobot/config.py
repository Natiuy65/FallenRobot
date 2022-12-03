class Config(object):
    LOGGER = True

    API_ID = 14443867
    API_HASH = "46ab81bdbf98137173153b27ec7904b2"
    TOKEN = "5779387408:AAG-6vQXl63-tbLOk0ELt1IKn_FKiebYsG8"
    OWNER_ID = 5448287981
    OWNER_USERNAME = "Nati_Sam223"
    SUPPORT_CHAT = "sn_robot_chat"
    JOIN_LOGGER = (-1001595694593)
    EVENT_LOGS = (-1001595694593)

    SQLALCHEMY_DATABASE_URI = ""
    MONGO_DB_URI = "mongodb+srv://ub:ub123@horivc.cemtd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 5448287981
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 5448287981
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 5448287981
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 5448287981
    WOLVES = 5448287981

    DONATION_LINK = "https://t.me/accounttool"
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = "-xyz"
    TIME_API_KEY = "-xyz"
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://te.legra.ph/file/f7858c819706c918b520e.jpg"
    HEROKU_API_KEY = 21f71571-10f2-4925-900f-9c9e3dce21be
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "VYLDJI-XGALDI-OUYEBG-JPPSPU-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
