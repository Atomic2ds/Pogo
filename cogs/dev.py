import discord
from discord.ext import commands
from discord import app_commands, ui, Webhook
global bot
from config import bot
from discord.app_commands import Choice
import pymongo
import random
from embeds import embedutil, errorembed
import requests
import traceback
import json
from typing import Optional
import io

import functions.dev as process
#import views.dev as view

class dev(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded the dev cog")


    # -- Dev Updates -- 
    @app_commands.command(name="update", description="Send an update for AP to the updates channel")
    @app_commands.describe(title="The title of the Update", description="What the update is about", mention="What role to mention on the update message", file="What file to attach to the update")
    async def updateslash(self, interaction: discord.Interaction, title: str, description: str, mention: Optional[discord.Role], file: Optional[discord.Attachment], channel: Optional[discord.TextChannel]):
      await process.send_update(interaction, title, description, mention, file, channel)


async def setup(bot):
    await bot.add_cog(dev(bot))
