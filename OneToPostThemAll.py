import discord
import requests
import json
import TikTakToe
from PIL import Image
from io import BytesIO
from discord.ext import commands
import os
from dotenv import load_dotenv

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
# @bot.event
# async def on_ready():
#     print(f'Bot is online! Logged in as {bot.user.name}')
#     # This part is to annoy my brother
#     user_id = 600748875707449374
#     channel = await bot.fetch_user(user_id)
#     await channel.send(f'I just wanted to tell you that you are pretty gay, {channel.mention}!')
#     print(f'{bot.user} is now online and has sent a message to {channel}!')

# Command: Greets the user when they type '!Hallo'
@bot.command(help='Greet me!')
async def Hallo(ctx):
    await ctx.send(f'Hallo wie kann ich dir behilflich sein, {ctx.author.mention}?')
    print(TikTakToe.game_Field[0])

# Command: Sends a "selfie" of the bot when the user types '!Selfie'
@bot.command(help='I will take a selfie!')
async def Selfie(ctx):
    img = bot.user.avatar
    await ctx.send(f'{img.url}')
    await ctx.send(f'Das bin ich! Sehe ich nicht süß aus? :blush:')

# Command: Fetches and sends a space status image from an API when the user types '!Spacestatus'
@bot.command(name="Spacestatus", help='Shows the space status')
async def Spacestatus(ctx):
    response = requests.get('https://spaceapi.n39.eu/state.png')
    img = BytesIO(response.content)
    await ctx.send(file=discord.File(img, filename='Status.png'))

# Command: Sends a link to the website when the user types '!Link'
@bot.command(name='Link', help='Shows the link to the website')
async def Link(ctx):
    await ctx.channel.send('https://www.netz39.de/')

@bot.command(name='Miau', help='Miau')
async def Furry(ctx):
    await ctx.channel.send('Miau :scream_cat:')
    
@bot.command(help='tick tack toe')
async def Test(ctx):
    TikTakToe.game_Field(ctx)

# Command: Sends some small update about current temperature and the weather to the User change latitute/longitute to your city to see current values from you location.
@bot.command(help= 'Whats the weather like in Magdeburg?')
async def Wetter(ctx):
    
    #Links for APIs --> Variable Names
    wetterAPILink = 'https://api.open-meteo.com/v1/forecast?latitude=52.1277&longitude=11.6292&current=temperature_2m,weather_code&forecast_days=1&models=icon_seamless'
    WMOTranslatorLink = 'https://gist.githubusercontent.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c/raw/76b0cb0ef0bfd8a2ec988aa54e30ecd1b483495d/descriptions.json'
    
    #fetching data from the weather api
    responseWeather_API = requests.get(wetterAPILink).json()
    
    #fetching data to translate weather codes (WMOs)
    resoponseWMO_API = requests.get(WMOTranslatorLink).json()
    await ctx.send(f'Im Moment beträgt die Temperatur in Magdeburg {responseWeather_API['current']['temperature_2m']}°C.\nZurzeit ist es {resoponseWMO_API[f'{responseWeather_API['current']['weather_code']}']['day']["description"]}.')

# Run the bot using the token from the environment variable
bot.run(f'{TOKEN}')
