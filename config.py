import os
from dotenv import load_dotenv

#Token
load_dotenv('token.env')
TOKEN = os.getenv('BOT_TOKEN')


# Server IDs
GUILD_ID = 1332833255996526652
#TEST_SERVER_ID = 

# Channel IDs
WELCOME_CHANNEL_ID = 1340257007009271860
#ANNOUNCEMENT_CHANNEL_ID = 
#MODERATION_CHANNEL_ID = 
#DAILY_QUESTION_CHANNEL_ID = 
#MEDITATION_REMINDER_CHANNEL_ID =
#REGION_OVERVIEW_CHANNEL_ID = 
#GAME_REACTIONROLES_CHANNEL_ID =

# Role IDs
#REGION_ROLES_IDS = 
#COOL_CLUBS_IDS = 
#CATEGORIES_ROLE_ID=


#COFFEE_CLUB_ID = 

# Other configurations
PREFIX = '!'
COOLDOWN_TIME = 3
MAX_WARNS = 3