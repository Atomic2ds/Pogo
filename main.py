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
from dotenv import load_dotenv
load_dotenv()
import os

class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or(">"), intents=intents)
    async def setup_hook(self) -> None:
       self.add_view(application_panel_buttons())
       self.add_view(learnmoreview())
       self.add_view(submittedview())
       self.add_view(rulesview())

bot = PersistentViewBot()

@bot.tree.command(name="rules",description="View the server rules in a nice embed")
async def rules(interaction: discord.Interaction):
   await interaction.response.send_message(embed=embedutil("rules","list"),view=rulesview(),ephemeral=True)

@bot.tree.command(name="ping",description="Get the ping of the Pogo bot")
async def ping(interaction: discord.Interaction):
   await interaction.response.defer(ephemeral=True)
   embed = discord.Embed(colour=0xFFFFFF, description=f"Pong! Connnections take {round(bot.latency * 1000)}ms")
   await interaction.followup.send(embed=embed,ephemeral=True)


class infoview(discord.ui.View):
   def __init__(self, label: str):
      super().__init__()
      self.label = label
      self.add_item(discord.ui.Button(label=self.label,style=discord.ButtonStyle.gray, disabled=True))

class commandgroups(discord.app_commands.Group):
  ...

@bot.event
async def on_ready():
    bot.tree.add_command(send)
    print(f"Connected to discord as {bot.user.name}")
    print("Syncing slash commands...")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} application (/) commands")
    except Exception as e:
        print(f"Unable to sync slash commands: {e}")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with ducks"))





send = commandgroups(name="send", description="Send a panel or an embed premade")

@send.command(name="application-panel", description="Use /form apply for slash command version")
async def application_panel(interaction: discord.Interaction):
   if interaction.user.id == 612522818294251522:
      try:
         embed = discord.Embed(colour=0xFFFFFF, title="Application Panel", description="Click the button below to apply for a bot to be made for you, we will host and manage everything for you")
         await interaction.channel.send(embed=embed, view=application_panel_buttons())
         await interaction.response.send_message("Successfully published the application panel",ephemeral=True)
      except Exception as e:
         await interaction.response.send_message(f"An error occured: {e}",ephemeral=True)
   else:
      await interaction.response.send_message("You don't have permission to run this command!",ephemeral=True)







class application_panel_buttons(discord.ui.View):
  def __init__(self):
     super().__init__(timeout=None)

  @discord.ui.button(label="Request a bot be made", style=discord.ButtonStyle.blurple, custom_id="application", emoji="📬")
  async def apply(self, interaction: discord.Interaction, button: discord.ui.Button):
     await interaction.response.send_modal(application())

  @discord.ui.button(label="Learn More", style=discord.ButtonStyle.gray, custom_id="learnmore", emoji="❔")
  async def learnmore(self, interaction: discord.Interaction, button: discord.ui.Button):
     await interaction.response.send_message(embed=embedutil("learn more","overview"),ephemeral=True,view=learnmoreview())


class learnmoreview(discord.ui.View):
   def __init__(self):
      super().__init__(timeout=None)
      self.add_item(learnmoredropdown())
      #self.add_item(discord.ui.Button(label="For more info contact Atomic2ds (Owner)",style=discord.ButtonStyle.gray, disabled=True, custom_id="contactatomic2dsdisabledbutton"))

class learnmoredropdown(discord.ui.Select):
  def __init__(self):
    options=[
      discord.SelectOption(label="Overview",description="A basic overview of how our hosting works", emoji="🏡"),
      discord.SelectOption(label="Hosting the bots",description="Learn how we host your bot and keep it secure", emoji="🌎"),
      discord.SelectOption(label="Application Process",description="Find out the process of getting your bot made", emoji="🪖"),
    ]

    super().__init__(placeholder="Choose a menu to view...", options=options, min_values=1, max_values=1, custom_id="learnmoredropdown")

  async def callback(self, interaction: discord.Interaction):
    if self.values[0] == "Overview":
       await interaction.response.edit_message(embed=embedutil("learn more","overview"),view=learnmoreview())
    elif self.values[0] == "Hosting the bots":
       await interaction.response.edit_message(embed=embedutil("learn more","hosting"),view=learnmoreview())
    elif self.values[0] == "Application Process":
       await interaction.response.edit_message(embed=embedutil("learn more","process"),view=learnmoreview())





class application(ui.Modal, title="Request a bot be made"):
    bot_name = ui.TextInput(label="Name", placeholder="What do you want your bot to be named?", style=discord.TextStyle.short, required=True)
    bot_function = ui.TextInput(label="Core Function", placeholder="What is the main thing your bot can do, this can go up to medium size", style=discord.TextStyle.long, required=True)
    bot_extras = ui.TextInput(label="Extra Features", placeholder="Anything else you want your bot to be able to do, for example a meme command", style=discord.TextStyle.long, required=False)

    async def on_submit(self, interaction: discord.Interaction):
       await interaction.response.defer(ephemeral=True)
       em = discord.Embed(colour=0xFFFFFF, title="Bot Creation Request", timestamp=datetime.datetime.utcnow())
       em.set_footer(text=interaction.user.id)
       em.add_field(name="1. What should your bot be named?",value=str(self.bot_name), inline=False)
       em.add_field(name="2. What should your bots core function be?",value=str(self.bot_function), inline=False)
       if not str(self.bot_extras) == "":
          em.add_field(name="2. What extra stuff do you want your bot to do?",value=str(self.bot_extras), inline=False)
       async with aiohttp.ClientSession() as session:
        #webhook = Webhook.from_url("https://discord.com/api/webhooks/1167644641143832616/GGwB_EtDqpbSIFnK57SSq3F8D6hksRei3wkQ2LhyAevI9Rjx9MqiA9BYhlpB_31pLv1g" ,session=session)
        channel = bot.get_channel(1190941122088947712)
        try:
            #username = interaction.user.name + "#" + interaction.user.discriminator
            #await webhook.send(embed=em,avatar_url=interaction.user.avatar,username=username)
            await channel.send(embed=em,view=infoview(f"Request sent in by {interaction.user.name.capitalize()}"))
            await interaction.followup.send("Successfully submitted a bot creation request, simply wait for us to dm you", ephemeral=True, view=submittedview())
        except Exception as e:
          await interaction.follwup.send(embed=errorembed(traceback.format_exc(), "/form"),epehmeral=True)

class submittedview(discord.ui.View):
  def __init__(self):
     super().__init__(timeout=None)

  @discord.ui.button(label="How this works", style=discord.ButtonStyle.gray, custom_id="application_process", emoji="❔")
  async def apply_process(self, interaction: discord.Interaction, button: discord.ui.Button):
     await interaction.response.send_message(embed=embedutil("learn more","process"),view=infoview("If your DMs are closed we can't make your bot"),ephemeral=True)






@send.command(name="rules-panel", description="Use /form apply for slash command version")
async def application_panel(interaction: discord.Interaction):
   if interaction.user.id == 612522818294251522:
      try:
         await interaction.channel.send(embed=embedutil("rules","list"),view=rulesview())
         await interaction.response.send_message("Successfully published the rules panel!",ephemeral=True)
      except Exception as e:
         await interaction.response.send_message(f"An error occured: {e}",ephemeral=True)
   else:
      await interaction.response.send_message("You don't have permission to run this command!",ephemeral=True)

class rulesview(discord.ui.View):
  def __init__(self):
     super().__init__(timeout=None)

  @discord.ui.button(label="Plaground Bot Rules", style=discord.ButtonStyle.gray, custom_id="bot_rules_button", emoji="🔮")
  async def bot_rules(self, interaction: discord.Interaction, button: discord.ui.Button):
     await interaction.response.send_message(embed=embedutil("rules","bot_rules"),ephemeral=True, view=application_panel_buttons())
  
  @discord.ui.button(label="Punishments", style=discord.ButtonStyle.gray, custom_id="punishments_button", emoji="🚁")
  async def punishments(self, interaction: discord.Interaction, button: discord.ui.Button):
     await interaction.response.send_message(embed=embedutil("rules","punishments"),ephemeral=True,view=infoview("Also we do not allow 'Mini-Modding' "))





@send.command(name="help-desk", description="Use /form apply for slash command version")
async def application_panel(interaction: discord.Interaction):
   if interaction.user.id == 612522818294251522:
      try:
         embed = discord.Embed(colour=0xFFFFFF, title="Help Desk", description="If your having issues understanding everything, or want clarification on something you can choose one of the options below")
         embed.add_field(inline=False,name="Making a ticket",value="Doing this will allow you to directly communicte with the staff team at Alexs Playground, here you can ask pretty much anything unless the staff refuse to answer")
         embed.add_field(inline=False,name="Opening the Documentation",value="You can open our documentation menu to view docs about Alexs Playground and get further insignt into how it works, with all of the inner workings exposed to you")
         await interaction.channel.send(embed=embed,view=helpdeskview())
         await interaction.response.send_message("Successfully published the help desk panel",ephemeral=True)
      except Exception as e:
         await interaction.response.send_message(f"An error occured: {e}",ephemeral=True)
   else:
      await interaction.response.send_message("You don't have permission to run this command!",ephemeral=True)


class helpdeskview(discord.ui.View):
  def __init__(self):
     super().__init__(timeout=None)

  @discord.ui.button(label="Open Documentation", style=discord.ButtonStyle.gray, custom_id="open_documentation", emoji="📑")
  async def punishments(self, interaction: discord.Interaction, button: discord.ui.Button):
     pass

  @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.gray, custom_id="open_ticket", emoji="🎫")
  async def bot_rules(self, interaction: discord.Interaction, button: discord.ui.Button):
     pass
  





def errorembed(message, command): 
  em = discord.Embed(title=f"An error occured -_-", description=f"There was an error when running {command}\nI have automaticlly reported the error to the Bot Devs```{message}```")
  return em

bot.run(os.environ["TOKEN"])