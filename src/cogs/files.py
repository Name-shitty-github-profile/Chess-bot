from nextcord.ext import commands
import os

class Files(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def reset(self):
    for j in ['svg', 'pics']:
      for i in os.listdir(j):
        os.remove(f'{j}/{i}')

def setup(bot):
  bot.add_cog(Files(bot))
