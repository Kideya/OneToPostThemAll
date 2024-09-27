import discord
#Spielfeld Inhalt erzeugen 3Zeilen/3Spalten
field = [[1,2,3],[4,5,6],[7,8,9]]
#Spielfeld grafik erzeugen
gamefield = f' {field[0][0]} | {field[1][0]} | 3 \n -----------\n 4 | 5 | 6\n -----------\n 7 | 8 | 9'

#Funktion für das Spielfeld erstellen
async def TikTakToe(ctx):
    global gamefield
    #Spielfeld mit Leeren werten füllen
    print (gamefield)
    #In Discord ausgeben
    await ctx.channel.send(f'``{gamefield}``')

##Input für den User erzeugen
#Buttons zum klicken erstellen
