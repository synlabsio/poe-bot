import discord
import asyncio
import os

#from discord.ext.commands import bot
from discord.ext import commands

#client = discord.Client()
bot = commands.Bot(command_prefix='!')

word_list = ['test', 'back']

@bot.event
async def on_ready():
  print('Bot is ready!')
  #print('we have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  if msg.startswith('$v') & any(word in msg for word in word_list):
    await message.channel.send('ON_MESSAGE: Hello1!')
    await message.channel.send('ON_MESSAGE: Hello2!')

  guild = message.guild
  
  if msg == "$count":
    await message.channel.send(f"""ON_MESSAGE: # of Members: {guild.member_count}""")
  
  await bot.process_commands(message)
  '''
  if msg.startswith('!List'):{
      for member in guild.members:
        print(member.name)
  }
  '''

@bot.command()
async def count(ctx):
  await ctx.send('ON_COMMAND: ReturnStringTest')

  
#client.run(os.environ['DiscordBotToken'])
bot.run(os.environ['DiscordBotToken'])
