import os
import discord
from dotenv import load_dotenv
from thes import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = int(os.getenv('CHANNEl'))
AUTHOR = int(os.getenv('AUTHOR'))

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    channel = client.get_channel(CHANNEL)
    await channel.send('ThesaurusizerBot is now awake')

    print(f'{client.user} is connected to the following guild:\n{guild.name}(id: {guild.id})', flush=True)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content == 'T: help':
        await message.channel.send('Welcome to the Thesaurusizer Bot!\nThis bot will take a word, phrase, or small paragraph and replace each uncommon word with a \"synonym\". Who needs grammarly when you have the Thesaurusizer to spice up your writing?\n\nUse \'T: \' to Thesaurusize your message.\n**Example**\nT: This is an example\n**Reply from ThesaurusizerBot**\nThis is an illustration')
    elif message.content[0:3] == 'T: ':
        if message.author.id == AUTHOR:
            if message.content == 'T: quit':
                channel = client.get_channel(CHANNEL)
                await channel.send('ThesaurusizerBot is now asleep')
                exit()
        try:
            thesMessage = thesMain(message.content)
            await message.reply(thesMessage)
        except:
            await message.reply('**Oops, error! :(**')


client.run(TOKEN)
