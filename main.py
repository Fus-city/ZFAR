import os
import discord
from discord.ext import commands

PREFIX = os.getenv('COMMAND_PREFIX')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(commands_prefix=PREFIX)

@bot.event
async def on_ready():
  print('Logged as :')
  print(bot.user.name)
  print(bot.user.id)
  print('-----')
 
 
@bot.event
async def on_message(message):
  msg = message.content
  athr = message.author
  chnl = message.channel
  
  if msg.startwith('.ping'):
    await chnl.send('Pong! :ping_pong:')
    
    
    
bot.run(TOKEN)
