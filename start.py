"""
Main entry point for the application.

This is where the bot is configured and launched.
"""

import nextcord
import os
import sys
import nextcord.ext.commands as commands
import nextcord.ext.tasks as tasks
import itertools
import dotenv


# |---------- CONFIG ----------|


dotenv.load_dotenv('files/.env')

intents = nextcord.Intents.all()
intents.members = True

prefix = "~"
colour = 0x486572
status = itertools.cycle(['~help', '~ai', '~play'])
client = commands.Bot(prefix, intents=intents, help_command=None, case_insensitive=True) # Help command = none so we can override it

PATH = './modules'
sys.path.append(PATH)

for module in os.listdir(PATH):
    if module.endswith('.py') and module not in ('__init__.py', 'helpers.py'):
        client.load_extension(f'modules.{module}'.replace('.py', ''))


# |----- BACKGROUND TASKS -----|


@tasks.loop(seconds=30)
async def change_presence():
    """
    Changes the bot's presence every 30 seconds.
    """
    activity = next(status)
    await client.change_presence(activity=nextcord.Game(activity))


# |---------- EVENTS ----------|


@client.event
async def on_ready():
    """
    Executes when the bot has loaded.
    """
    print(f"Loaded {client.user.name} successfully.")
    await change_presence.start()


# |---------- LAUNCH ----------|


TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
