import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'LuciferMoringstar_Robot')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", "-1001729830342"))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())
DB_URL = os.environ.get("DATABASE_1", "")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = -1001702519740
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
TUTORIAL = "https://t.me/piro_tuts"
# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Files")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**𝖸𝗈...𝖸𝗈... 💖

𝖨'𝗆 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖠𝗎𝗍𝗈-𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖬𝖾 𝖠𝗌 𝖠 𝖠𝗎𝗍𝗈-𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉

𝖨𝗍𝗌 𝖤𝖺𝗌𝗒 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾; 𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇, 
𝖳𝗁𝖺𝗍𝗌 𝖠𝗅𝗅, 𝗂 𝗐𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖳𝗁𝖾𝗋𝖾...🤓🤪


⚠️𝖬𝗈𝗋𝖾 𝖧𝖾𝗅𝗉 𝖢𝗁𝖾𝖼𝗄 𝖧𝖾𝗅𝗉 𝖡𝗎𝗍𝗍𝗈𝗇 𝖡𝖾𝗅𝗈𝗐

🙋🏻‍♂️ 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅 𝖦𝗎𝗂𝖽𝖾 @piro_tuts

😎 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 @rai_info17"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "📂 <em>File Name</em>: <code>PIRO|{file_name}</code> \n\n\n❤️‍🔥 </i>Join</i> [𝗕𝗟𝗔𝗦𝗧𝗘𝗥 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 ;)](https://t.me/blasters_monthly)  \n\n\n🖥 <i>Requests</i> - ||@raixpiro_bot||")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
