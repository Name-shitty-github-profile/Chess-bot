import nextcord
from nextcord.ext import commands

class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "info", description = "Some info about the creator and the bot")
  async def info_slash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(embed=nextcord.Embed(title="Info", description=f"**Guilds** : {len(self.bot.guilds)}\n**Identity**\nA canadian blond girl named Noémie\n\n**Projects that she is in**\n\n[Amnesia Network](https://discord.gg/amnesianetwork)\n\n[Minecraft server](https://discord.gg/j38sVck9AB)\n\n[Horizon](https://discord.gg/Rs7NS9YcNB)\n\nThis bot took 2 days to make", color=0x206694))

def setup(bot):
  bot.add_cog(Info(bot))
