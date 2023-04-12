import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "6280972722:AAEXoHSgIGa8wcIywcI__iccVN88OE8t9LQ") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 17983098)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "ee28199396e0925f1f44d945ac174f64") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1227193881)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://Bala7a19871:Ibntaymya1.@cluster0.5mtsc.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
