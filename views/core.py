import discord

class infoview(discord.ui.View):
   def __init__(self, label: str):
      super().__init__()
      self.label = label
      self.add_item(discord.ui.Button(label=self.label,style=discord.ButtonStyle.gray, disabled=True))