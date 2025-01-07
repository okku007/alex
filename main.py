import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot= commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx,*,arg):
    await ctx.send(arg)


print(f"Prefix is {bot.command_prefix}")    
bot.run('your token here!') 