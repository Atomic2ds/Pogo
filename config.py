import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

try:
    TOKEN = os.environ["TOKEN"]
except:
    TOKEN = None

class BotClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or(">"), intents=intents)
    async def setup_hook(self) -> None:
       from views.send import application_panel_buttons, learnmoreview, submittedview, rulesview
       self.add_view(application_panel_buttons())
       self.add_view(learnmoreview())
       self.add_view(submittedview())
       self.add_view(rulesview())

bot = BotClient()
