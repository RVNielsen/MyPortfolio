import os
import discord
from dotenv import load_dotenv
from thes import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n{guild.name}(id: {guild.id})', flush=True)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content[0:3] == 'T: ':
        try:
            thesMessage = thesMain(message.content)
            await message.reply(thesMessage)
        except:
            await message.reply('**Oops, error! :(**')

    if message.content == 'T: help':
        await message.channel.send('Welcome to the Thesaurusizer Bot!\nThis bot will take a word, phrase, or small paragraph and replace each uncommon word with a \"synonym\". Who needs grammarly when you have this to spice up your writing?\n\nUse \'T: \' to Thesaurusize your message.\n**Example**\nT: This is an example\n**Reply from ThesaurusizerBot**\nThis is an illustration\n\nThings that will break the bot include:\n-Excessively long non-words\n-Newlines\n-Uncommon characters')

client.run(TOKEN)
