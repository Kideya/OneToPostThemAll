import discord

async def AnnoySomeone(bot):
    # This part is to annoy someone
    
    #insert User ID (needs to be on the same Discord as the bot)
    user_id = 226853269291401216
    channel = await bot.fetch_user(user_id)
    await channel.send(f'I just wanted to tell you that you are pretty gay, {channel.mention}!')
    print(f'{bot.user} is now online and has sent a message to {channel}!')
    
def Miau(bot):
    @bot.command(name='Miau', help='Miau')
    async def Miau(ctx):
        await ctx.channel.send('Miau :scream_cat:')
    
    
def Selfie(bot):
    @bot.command(help='I will take a selfie!')
    async def Selfie(ctx):
        img = bot.user.avatar
        await ctx.send(f'{img.url}')
        await ctx.send(f'Das bin ich! Sehe ich nicht süß aus? :blush:')

def Hallo(bot):
    @bot.command(help='Greet me!')
    async def Hallo(ctx):
        await ctx.send(f'Hallo wie kann ich dir behilflich sein, {ctx.author.mention}?')