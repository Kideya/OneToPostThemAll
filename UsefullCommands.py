import requests
import discord
from io import BytesIO

def Spacestatus(bot):
    @bot.command(name="Spacestatus", help='Shows the space status')
    async def Spacestatus(ctx):
        response = requests.get('https://spaceapi.n39.eu/state.png')
        img = BytesIO(response.content)
        await ctx.send(file=discord.File(img, filename='Status.png'))
        
def WebsiteLink(bot):
    @bot.command(name='Link', help='Shows the link to the website')
    async def Link(ctx):
        await ctx.channel.send('https://www.netz39.de/')
 
def Weather(bot):
    @bot.command(name='Wetter', help= 'Whats the weather like in Magdeburg?')
    async def Wetter(ctx):       
        #Links for APIs --> Variable Names
        wetterAPILink = 'https://api.open-meteo.com/v1/forecast?latitude=52.1277&longitude=11.6292&current=temperature_2m,weather_code&forecast_days=1&models=icon_seamless'
        WMOTranslatorLink = 'https://gist.githubusercontent.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c/raw/76b0cb0ef0bfd8a2ec988aa54e30ecd1b483495d/descriptions.json'
        
        #fetching data from the weather api
        responseWeather_API = requests.get(wetterAPILink).json()
        
        #fetching data to translate weather codes (WMOs)
        resoponseWMO_API = requests.get(WMOTranslatorLink).json()
        await ctx.send(f'Im Moment beträgt die Temperatur in Magdeburg {responseWeather_API['current']['temperature_2m']}°C.\nZurzeit ist es {resoponseWMO_API[f'{responseWeather_API['current']['weather_code']}']['day']["description"]}.')