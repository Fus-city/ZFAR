import time
import random
import discord
from discord.ext import commands

TOKEN = ''
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('Logged as :')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

@bot.event
async def on_message(message):
    msg = message.content
    ch = message.channel
    athr = message.author
    guild = message.guild

#   Couleurs
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    if msg.startswith("*say"):
        op = msg.split("*say")
        await ch.send(op[1])

    if msg == "*ping":
        await ch.send('Pong! :ping_pong:')
    
    if msg == "*help":

        embed = discord.Embed(title="Commande d'aide activé", description="Syntaxe de l'aide : *help <commande>", color=0x24ff54)
        embed.set_author(name=athr, icon_url=athr.avatar_url)
        embed.add_field(name="poll", value="Faire un sondage", inline=False)
        embed.add_field(name="say", value="Juste répéter", inline=False)
        embed.set_footer(text="Fait par Fusity#1924 || https://discord.gg/x9syZxG")

        await ch.send(embed=embed)

    if msg.startswith("*help"):
        msg2 = msg.split(" ")
        msg3 = msg2[1]

        if msg3 == "poll":
            embed = discord.Embed(title=msg3, description="Syntaxe de la commande : " + msg3 + "<Question>, <Réponse 1>, <Réponse 2>")
            embed.add_field(name=msg3, value="""Veillez à entrer une commande correcte : (Ne pas oublier les ",")""", inline=False)
            embed.add_field(name="*poll Pain au chocolat ou chocolatine ?, Pain au chocolat, Chocolatine", value="Se qui donnera :")
            await ch.send(embed=embed)
            time.sleep(1)
            await ch.send("*poll Pain au chocolat ou chocolatine ?, Pain au chocolat, Chocolatine")

    if msg.startswith("*kick"):
        a = msg.split(" ", 2)
        if not len(a) == 3:
            a.insert(2, "Non renseigné")
        reason = a[2]

        await ch.send(message.mentions)
#        for user in message.mentions:
#            target = user.id
        await athr.kick(message.mentions, reason=reason)
        await bot.say('Utilisateur {} a été kick du serveur par {}, raison : "*{}*"'.format(message.mentions, athr, reason))



    if msg.startswith("*poll"):
        msg2 = msg.split("*poll")
        q = msg2[1].split(",")
        
#        if q[0] == False:
#            await ch.send("Rentrez une question et ses réponses (5 max.)")
        question = q[0]
        
#        if q[1] == False:
#            await ch.send("Rentrez une question et ses réponses (5 max.)")
        reponse1 = q[1]

#        if q[2] == False:
#            await ch.send("Rentrez une question et ses réponses (5 max.)")
        reponse2 = q[2]

#        if q[3] == False:
#            q[3] = "The void"
#        reponse3 = q[3]
        
#        if q[4] == False:
#            q[4] = "The void"
#        reponse4 = q[4]

        #reponse5 = q[5]

        color = (random.randint(0, 0xffffff))#, random.randint(0, 255), random.randint(0, 255))

#        random_number = random.randint(0,16777215)
#        hex_number = str(hex(random_number))
#        color ='#'+ hex_number[2:]

        embed=discord.Embed(title="Question :thinking:", description="Répondez grâce aux emojis !", color=color)
        embed.set_author(name=athr, icon_url=athr.avatar_url)
        embed.add_field(name=":regional_indicator_p::regional_indicator_o::regional_indicator_l::regional_indicator_l:", value=question, inline=False)
        embed.add_field(name=":one:", value=reponse1, inline=False)
        embed.add_field(name=":two:", value=reponse2, inline=False)
#        embed.add_field(name=reponse3, value=":three:", inline=False)
        embed.set_footer(text="Fait par Fusity#1924")
        await message.delete()
        await ch.send(embed=embed)
#        await msg.add_reaction("1️⃣")
#        await msg.add_reaction("2️⃣")




bot.run(TOKEN)