import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT')
GUILD = os.getenv('DISCORD_GUILD')