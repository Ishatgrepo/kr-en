import os, time, re

id_pattern = re.compile(r'^.\d+$') 
from os import environ


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "14050586")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8152265435:AAFo3fICFb6HwNA396hW09oZjqwQ0mpZgS0") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'napoleonfile') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6469067345")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002462991438')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/219c7ce28f8f9262c3477-5ac482fb1d0adadca5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
    # token
    API = environ.get("API", "d3b719a450497b8ccf8a1f2d0b1e38ecad78e3c5") # shortlink api
    URL = environ.get("URL", "https://anylinks.in") # shortlink domain without https://
    VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/Testinhhhhhbot") # how to open link 
    BOT_USERNAME = environ.get("BOT_USERNAME", "Rdpmodibot") # bot username without @
    VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.


    caption = """
🚀 **File Successfully Processed!** 🌟  

📂 **File Name:** `{0}` 📝✨  
📏 **Original Size:** `{1}` 📦📏  
🗜 **Encoded Size:** `{2}` 🔐💾  
📉 **Compression:** `{3}%` 📊🔽  

⏬ **Downloaded in:** `{4}` ⏳📥  
⚙️ **Encoded in:** `{5}` ⚡🎛  
☁️ **Uploaded in:** `{6}` 🚀📤  

🔥 **Your file is compressed, optimized, and ready to go!** 😎✨
"""
