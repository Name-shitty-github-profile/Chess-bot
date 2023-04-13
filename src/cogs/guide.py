import nextcord
from nextcord.ext import commands

class Guide(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "how", description = "How to play with the bot?")
  async def how_to_play_slash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(embed=nextcord.Embed(title="How to play?", description="**Play a move**\nThe way we can play a move is by saying play <the move>\nAll moves are in [UCI](https://www.dcode.fr/uci-chess-notation#:~:text=The%20UCI%20format%20describes%20the,digit%2C%20letter%2C%20digit) or [Algebraic](https://www.chess.com/article/view/chess-notation#algebraic-notation)\n\n**Draw**\nHow can we propose a draw?\nYou only say draw when it's your turn !\nThe person have to accept or refuse\n\n**Resign**\nTo resign you only say resign or abort\n\n**Abort**\n\nTo abort you only say resign or abort in the start of the game", color=0x206694))

def setup(bot):
  bot.add_cog(Guide(bot))
