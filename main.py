from ast import ExceptHandler
from calendar import EPOCH
from pydoc import describe
from xml.dom.expatbuilder import parseString
import discord
from discord.ext import commands
import datetime
import aiohttp
from discord import Webhook, ui
import random
import json
import traceback
import asyncio
from embeds import embedutil
from config import bot
import config
import os 


class commandgroups(discord.app_commands.Group):
  ...

@bot.event
async def on_ready():
    print(f"Connected to discord as {bot.user.name}")
    print("Syncing slash commands...")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} application (/) commands")
    except Exception as e:
        print(f"Unable to sync slash commands: {e}")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with ducks"))
  

async def main():
    await load()
    if config.TOKEN == None:
      print("Unable to boot the bot, no token env was set")
    else:
      await bot.start(config.TOKEN)

async def load():
  for file in os.listdir('./cogs'):
    if file.endswith('.py'):
      await bot.load_extension(f'cogs.{file[:-3]}')

asyncio.run(main())

bot.run(os.environ["TOKEN"])