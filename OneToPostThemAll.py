import discord
import requests
import json
from PIL import Image
from io import BytesIO
from discord.ext import commands
import os
from dotenv import load_dotenv

import FunCommands as fun
import UsefullCommands as QoL
import TikTakToe



# Load the .env file that contains your bot token
load_dotenv('/home/kideya/OneToPostThemAll/test-env/.env')

# Get your bot token from the environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Create intents, which are needed to access certain events such as messages
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# Initialize the bot with a command prefix '!' and the defined intents
bot = commands.Bot(command_prefix='!', intents=intents)

# This event is triggered when the bot is ready (connected to Discord and logged in)
@bot.event
async def on_ready():
    print(f'Bot is online! Logged in as {bot.user.name}')
    # await fun.AnnoySomeone(bot)

                                             #FUN COMMANDS#
###################################################################################################################

# Command: Greets the user when they type '!Hallo'
fun.Hallo(bot)
# Command: Sends a "selfie" of the bot when the user types '!Selfie'
fun.Selfie(bot)
# Command: Sends a Miau to the Author of the Message
fun.Miau(bot)

                                            #USEFULL COMMANDS#
###################################################################################################################

# Command: Fetches and sends a space status image from an API when the user types '!Spacestatus'
QoL.Spacestatus(bot)

# Command: Sends a link to the website when the user types '!Link'
QoL.WebsiteLink(bot)

# Command: Sends some small update about current temperature and the weather to the User change latitute/longitute to your city to see current values from you location.
QoL.Weather(bot)

@bot.command(help='tick tack toe')
async def Test(ctx):
    await TikTakToe.TikTakToe(ctx)

    
# Run the bot using the token from the environment variable
bot.run(f'{TOKEN}')
