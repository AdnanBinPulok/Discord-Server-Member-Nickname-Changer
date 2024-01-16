import discord
from discord.ext import commands
import json
import random

bot = commands.Bot(
    command_prefix='!',
    intents=discord.Intents.all(),
    case_insensitive=True
)

with open('./settings/config.json', 'r') as f:  
    config_data= json.load(f)



guild_id = config_data.get('guild_id')


with open('./src/names.txt', 'r') as f:
    names= f.read().splitlines()



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await change_nick_loop()


async def change_nick_loop():
    guild = bot.get_guild(guild_id)
    for member in guild.members:
        try:
            nickname = random.choice(names)
            await member.edit(nick=nickname)
            print(f"{member}'s nickname changed to {nickname}")
        except Exception as e:
            print(e)
    
    print("Nickname changing loop finished")

bot.run(config_data.get('token'))