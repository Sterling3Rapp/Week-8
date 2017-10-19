import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.
BOT_IDENTITY = {'token': 'xoxb-258851594883-LNl9PMnfqZ6GaiMutHdO3m0t',}




BOT_DATA_DIR = r'/Users/cecil/Documents/untitled/data'
BOT_EXTRA_PLUGIN_DIR = r'/Users/cecil/Documents/untitled/plugins'

BOT_LOG_FILE = r'/Users/cecil/Documents/untitled/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@sterling3rappbot', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!
BOT_ALT_PREFIXES = ('@sterling3rappbot',)
CHATROOM_PRESENCE = ()