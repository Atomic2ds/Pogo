import discord
from embeds import embedutil, errorembed
import traceback
from views.core import infoview
import aiohttp
from discord import ui
from config import bot
import datetime

# -- Application Panel -- 

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

# -- Help Desk -- 
     
class helpdeskview(discord.ui.View):
  def __init__(self):
     super().__init__(timeout=None)

  @discord.ui.button(label="Open Documentation", style=discord.ButtonStyle.gray, custom_id="open_documentation", emoji="📑")
  async def punishments(self, interaction: discord.Interaction, button: discord.ui.Button):
     pass

  @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.gray, custom_id="open_ticket", emoji="🎫")
  async def bot_rules(self, interaction: discord.Interaction, button: discord.ui.Button):
     pass
  

# -- Rules Panel -- 
  
class rulesview(discord.ui.View):
  def __init__(self):
     super().__init__(timeout=None)

  @discord.ui.button(label="Plaground Bot Rules", style=discord.ButtonStyle.gray, custom_id="bot_rules_button", emoji="🔮")
  async def bot_rules(self, interaction: discord.Interaction, button: discord.ui.Button):
     await interaction.response.send_message(embed=embedutil("rules","bot_rules"),ephemeral=True, view=application_panel_buttons())
  
  @discord.ui.button(label="Punishments", style=discord.ButtonStyle.gray, custom_id="punishments_button", emoji="🚁")
  async def punishments(self, interaction: discord.Interaction, button: discord.ui.Button):
     await interaction.response.send_message(embed=embedutil("rules","punishments"),ephemeral=True,view=infoview("Also we do not allow 'Mini-Modding' "))
