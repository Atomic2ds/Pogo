import discord
from discord.ext import commands
from discord import app_commands, ui, Webhook
global bot
from config import bot
from discord.app_commands import Choice
import pymongo
import random
from embeds import embedutil
import requests
import traceback
import json

import functions.send as process
import views.send as view

class send(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded the send cog")

    send = app_commands.Group(name="send", description="Send a panel")

    # -- Application Panel -- 
    @send.command(name="application-panel", description="Use /form apply for slash command version")
    async def application_panel(self,interaction: discord.Interaction):
        await process.application_panel(interaction,view)

    # -- Help Desk -- 
    @send.command(name="help-desk", description="Use /form apply for slash command version")
    async def help_desk(self,interaction: discord.Interaction):
      await process.help_desk(interaction,view)

    # -- Rules Panel --
    @send.command(name="rules-panel", description="Use /form apply for slash command version")
    async def application_panel(self,interaction: discord.Interaction):
       await process.rules_panel(interaction,view)

async def setup(bot):
    await bot.add_cog(send(bot))
