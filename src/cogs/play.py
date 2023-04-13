import nextcord
from nextcord.ext import commands
import chess
from utils import Sending, Move_collector
from elo import win, draw, get_elo
next = {
  0: 1,
  1: 0
}

class Play(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "play", description = "Play chess")
  async def play_slash(self, interaction: nextcord.Interaction, member: nextcord.User = nextcord.SlashOption(name="membre", description="Your opponent"), channel: nextcord.TextChannel = nextcord.SlashOption(name="channel", description="The channel of the game", required=False), ranked: bool = nextcord.SlashOption(name="ranked", description="Is the game ranked?", required=False)):
    if member.id == interaction.user.id:
      await interaction.response.send_message("You can't play with yourself..")
      return
    await interaction.response.send_message(f"{interaction.user.mention} (White) ({get_elo(interaction.user.id)} elo) **VS** {member.mention} (Black) ({get_elo(member.id)} elo)")
    if ranked is None: ranked = True
    board = chess.Board()
    turn = 0
    players = [
      {"couleur": chess.WHITE, "id": interaction.user.id, 'name': interaction.user.name},
      {"couleur": chess.BLACK, "id": member.id, "name": member.name}
    ]
    opponent = player = None
    if channel is None: channel = interaction.channel
    mover = Move_collector(channel, self.bot)
    send = Sending(channel)
    while board.is_checkmate() is False and board.is_stalemate() is False and board.is_insufficient_material() is False:
      player = players[turn]
      await send.send(f'It\'s the turn of {player["name"]}!', board, player['couleur'])
      move = await mover.collect(player['id'], board)
      if move == 'resign':
        if opponent is None:
          await send.send('**Game aborted**', board, player['couleur'])
          return
        await send.send(f"The winner is {player['name']} !!!\n(Resigned)", board, player['couleur'])
        send.end()
        win(opponent['id'], player['id'])
        return
      elif move == 'draw':
        if opponent is None:
          await send.send('**Game aborted**', board, player['couleur'])
          return
        await channel.send(f"{player['name']} is proposing a draw what do you say?")
        def check(m):
          return m.author.id == opponent['id'] and m.channel.id == channel.id and m.content.lower() in ['n', 'no', 'y', 'yes', 'ye']
        msg = await self.bot.wait_for('message', check=check)
        if msg.content in ['n', 'no']:
          await channel.send("**They didn't accept !**")
          while move not in ['resign', 'draw']:
            move = await mover.collect(player['id'], board)
            if move == 'resign':
              await send.send(f"The winner is {player['name']} !!!\n(Resigned)", board, player['couleur'])
              send.end()
              if ranked: win(opponent['id'], player['id'])
              return
            elif move == 'draw':
              await channel.send("You cannot ask for another draw!\nPlease wait a turn!")
        else:
          await send.send('**Draw**', board, player['couleur'])
          if ranked: draw(player['id'], opponent['id'])
          return
      board.push(move)
      opponent = player
      turn = next[turn]
    if board.is_checkmate():
      await send.send(f"The winner is {player['name']} !!!", board, player['couleur'])
      if ranked: win(opponent['id'], player['id'])
    elif board.is_stalemate():
      await send.send('**Stalemate**', board, player['couleur'])
      if ranked: draw(player['id'], opponent['id'])
    elif board.is_insufficient_material():
      await send.send('**Insufficient material**', board, player['couleur'])
      if ranked: draw(player['id'], opponent['id'])
    send.end()
    

def setup(bot):
  bot.add_cog(Play(bot))
