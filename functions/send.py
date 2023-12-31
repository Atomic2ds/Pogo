from config import bot
from embeds import embedutil
import discord

# -- Rules Panel -- 

async def rules_panel(interaction, view):
    if interaction.user.id == 612522818294251522:
      try:
        await interaction.channel.send(embed=embedutil("rules","list"),view=view.rulesview())
        await interaction.response.send_message("Successfully published the rules panel!",ephemeral=True)
      except Exception as e:
        await interaction.response.send_message(f"An error occured: {e}",ephemeral=True)
    else:
        await interaction.response.send_message("You don't have permission to run this command!",ephemeral=True)

# -- Help Desk -- 
async def help_desk(interaction,view):
      if interaction.user.id == 612522818294251522:
        try:
         embed = discord.Embed(colour=0xFFFFFF, title="Help Desk", description="If your having issues understanding everything, or want clarification on something you can choose one of the options below")
         embed.add_field(inline=False,name="Making a ticket",value="Doing this will allow you to directly communicte with the staff team at Alexs Playground, here you can ask pretty much anything unless the staff refuse to answer")
         embed.add_field(inline=False,name="Opening the Documentation",value="You can open our documentation menu to view docs about Alexs Playground and get further insignt into how it works, with all of the inner workings exposed to you")
         await interaction.channel.send(embed=embed,view=view.helpdeskview())
         await interaction.response.send_message("Successfully published the help desk panel",ephemeral=True)
        except Exception as e:
         await interaction.response.send_message(f"An error occured: {e}",ephemeral=True)
      else:
        await interaction.response.send_message("You don't have permission to run this command!",ephemeral=True)

# -- Application Panel -- 
async def application_panel(interaction,view):
      if interaction.user.id == 612522818294251522:
        try:
         embed = discord.Embed(colour=0xFFFFFF, title="Application Panel", description="Click the button below to apply for a bot to be made for you, we will host and manage everything for you")
         await interaction.channel.send(embed=embed, view=view.application_panel_buttons())
         await interaction.response.send_message("Successfully published the application panel",ephemeral=True)
        except Exception as e:
         await interaction.response.send_message(f"An error occured: {e}",ephemeral=True)
      else:
        await interaction.response.send_message("You don't have permission to run this command!",ephemeral=True)