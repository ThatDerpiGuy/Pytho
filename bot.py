import discord
from discord.ext import commands


TOKEN = 'NjkxMDg3OTAxMTk4NTE2Mjk1.Xna3yg.lGvEeFTlN1MmL8QaSao-nVIOK9A'

client = commands.Bot(command_prefix = '~')

@client.event
async def on_ready():
    print('Ready!')
    

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def info(ctx):
    await ctx.send('This bot was made by Derpi in Python 3.8, hence the name Pytho.')

@client.command()
async def say(ctx, *, arg):
    await ctx.send(arg)





client.run(TOKEN)