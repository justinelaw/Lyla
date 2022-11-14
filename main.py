import discord
import random
from discord.ext import commands
import os
from dotenv import load_dotenv
#import youtube_dl

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event 
async def on_ready():
        print('Logged on as {0}'.format(bot.user))
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Pied Piper by BTS"))
@bot.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)

@bot.command(name= 'test', help= 'Test command')
async def test(ctx):
    text = "hello"
    await ctx.send(text)

#note: for future music category/cog
@bot.command(name='join', help='Bot will join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name= 'info', help= 'Shows server information and statistics')
async def info(ctx):
    serverName = str(ctx.guild.name)
    embed = discord.Embed(title= serverName + ' - Server Information', color= discord.Color.purple())
    serverID = str(ctx.guild.id)
    owner = str(ctx.guild.owner)
    members = str(ctx.guild.member_count)
    create_time = ctx.guild.created_at
    dateOfCreation = str(create_time.month) + '/' + str(create_time.day) + '/' + str(create_time.year)

    embed.add_field(name = 'Owner: ', value = owner, inline = True)
    embed.add_field(name = 'Member count: ', value = members, inline = True)
    embed.add_field(name = "Date created: ", value = dateOfCreation, inline = True)
    embed.add_field(name = 'Server ID: ', value = serverID, inline = True )

    await ctx.send(embed=embed)



bot.run(TOKEN)