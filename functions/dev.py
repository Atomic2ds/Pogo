from embeds import embedutil, errorembed
import traceback
import discord, io
global bot
from config import bot

# -- Dev Updates -- 
async def send_update(interaction, title, description, mention, file, channel):
    try:
         await interaction.response.defer(ephemeral=True)

         if interaction.user.id == 612522818294251522:
           if channel == None:
             channel = bot.get_channel(1190983883009839145)
           embed = embedutil("core",("update",f"{title} <:9582_announce:1173479624412508202>",description,interaction))

           if mention:
            content = f"<@&{mention.id}>"
           else:
            content = None

           if content:
            await channel.send(content, embed=embed)
           else:
            await channel.send(embed=embed)

            if file:
                file_data = await file.read()
                file_obj = discord.File(io.BytesIO(file_data), filename=file.filename)
                try:
                   await channel.send(file=file_obj)
                except:
                   pass
            
           await interaction.followup.send("Successfully send the pogo update")

         else:
          await interaction.followup.send("Only official pogo devs can use this command")

    except Exception:
         await interaction.followup.send(embed=errorembed(traceback.format_exc(),"/update"))