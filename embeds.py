import discord


def embedutil(name, content):
    if name == "learn more":
        if content == "overview":
            embed = discord.Embed(colour=0xFFFFFF, title="How our playground server works", description="You can apply for a bot to be made and we will make it for you, host it for you, update it for you and basically manage everything for you.")
            embed.add_field(name="You should know",value="We cannot make anything big, like a big public bot with a web dashboard, custom domain and all that we just make simple little fun bots as a hobby project")
        elif content == "hosting":
            embed = discord.Embed(colour=0xFFFFFF, title="How we host the bots", description="We host your bots on a premium virtual private server in Frankfurt, Germany with 1Gbit networking, high performance 3.60GHz CPU and Raid1 NVMe Storage with daily backups going back 5 days")
        elif content == "process":
            embed = discord.Embed(colour=0xFFFFFF, title="How the application process works", description="Once we review your bot creation request, we will dm you letting you know if your bot is being created or if your bot is not being created. We will then tell you an eta of how long it will take. Once your bot is finished we will dm you an invite link to your bot and will let you know when its finished")

    if name == "rules":
        if content == "punishments":
            embed = discord.Embed(colour=0xFFFFFF, title="How punishments work", description="You will be punished for breaking the rules entirely depending on the situation and severity of the issue. Staff will decide punishments on a per sitution basis and there are no strict punishments in place")

        if content == "bot_rules":
            embed = discord.Embed(colour=0xFFFFFF, title="Rules with playground bots", description="When requesting for a playground bot to be made, consider these rules")
            embed.add_field(inline=False,name="Nothing illegal",value="We will not make anything that is considered illegal even if you agree to take full responsibility for it or if you own the bot itself we will still refuse to make it")
            embed.add_field(inline=False,name="Nothing against TOS",value="We will refuse to make anything that is against Discord's terms of service, we don't wanna be banned off the platform and have all of our other bots terminated")

        if content == "list":
            embed = discord.Embed(colour=0xFFFFFF, title="General Server Rules", description="Below are some simple rules everyone in the server must follow")
            embed.add_field(inline=False,name="No spamming any chanels",value="Any sort of spam, no matter if its just spam message sending or just flooding the chat with long messages will not be tolerated in any of the chats")
            embed.add_field(inline=False,name="No self-promotion",value="You are only allowed to send things like server invites, bot invites if you have explicit permission from the owner, otherwise its not allowed in any way")
            embed.add_field(inline=False,name="Be Respectful to server members",value="Don't be a bitch and constantly make fun of, mock or make fun of someone for something irrelevant or small")
            embed.add_field(inline=False,name="No doxxing or exposing personal info",value="You are not allowed to send other peoples personal information to chat like peoples ip addresses, house addresses, peoples fact or any of that")

    if name == "core":
        if content[0] == "update":
            title = content[1]
            description = content[2]
            interaction = content[3]
            embed = discord.Embed(title=title, description=description, colour=0xFFFFFF)
            embed.set_author(name=interaction.user.name.capitalize() + "・Staff Member", icon_url=interaction.user.avatar)
            embed.set_footer(text=interaction.guild.name)

    return embed


def errorembed(message, command): 
  em = discord.Embed(title=f"An error occured -_-", description=f"There was an error when running {command}\nI have automaticlly reported the error to the Bot Devs```{message}```")
  return em