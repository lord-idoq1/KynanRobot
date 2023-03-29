class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "27702445"
    API_HASH = "ee51cbc025f446a5ed8a3cb8ba31795a"

    CASH_API_KEY = "SADHAZ7VT717K66N"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://idlnkhzekxplbu:89bee2931c762d3db975316ee5a5cf5251a919813ba4ece1eb5ba665ef59cda4@ec2-54-197-23-105.compute-1.amazonaws.com:5432/dfvckidh72nilk"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://marko:mSOAUhiWxozTz4a6@cluster0.gzsfr0m.mongodb.net"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/4c55a821a21d9eddebf70.jpg"
    
    DONATE_LINK = "https://graph.org/file/2982a27fe0e1500bf5b17.jpg"

    SUPPORT_CHAT = "+vpGZKznd9n83MjE1"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5908998341:AAF1SoeBXlPh-mhf1sPeUtLhbcAexatlv6s"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "SNQTVJDIAPVM"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "1976061168"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    OWNER_USERNAME = "aypnybe"
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
