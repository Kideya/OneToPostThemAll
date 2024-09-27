import discord as dc
#Spielfeld Inhalt erzeugen 3Zeilen/3Spalten
field = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#Spielfeld grafik erzeugen
gamefield =f'\
 {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
-----------\n\
 {field[1][0]} | {field[1][1]} | {field[1][2]} \n\
-----------\n\
 {field[2][0]} | {field[2][1]} | {field[2][2]} '

#Funktion für das Spielfeld erstellen
async def TikTakToe(ctx):
    global gamefield
    #In Discord ausgeben
    # message = await ctx.channel.send(f'```{gamefield}```')
    # emoji = ':one:'
    # await message.add_reaction(emoji)
    message = await ctx.send('Hier ist eine Nachricht mit einem Emoji!')
      # Du kannst jedes Emoji hinzufügen
    # await message.add_reaction("\U+0031")
##Input für den User erzeugen

#Buttons zum klicken erstellen