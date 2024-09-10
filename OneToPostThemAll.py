import discord
import requests
from PIL import Image
from io import BytesIO
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load the .env file that contains your bot token
load_dotenv()

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
    # This part is to annoy my brother
    # user_id = 600748875707449374
    # channel = await bot.fetch_user(user_id)
    # await channel.send(f'I just wanted to tell you that you are pretty gay, {channel.mention}!')
    # print(f'{bot.user} is now online and has sent a message to {channel}!')

# Command: Greets the user when they type '!Hallo'
@bot.command(help='Greet me!')
async def Hallo(ctx):
    await ctx.send(f'Hallo wie kann ich dir behilflich sein, {ctx.author.mention}?')

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

# Run the bot using the token from the environment variable
bot.run(TOKEN)