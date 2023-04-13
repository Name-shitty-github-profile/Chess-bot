import chess
class Move_collector:
  def __init__(self, channel, bot):
    self.channel = channel
    self.bot = bot

  async def translate_move(self, content, board):
    if content.lower().startswith('resign') or content.lower().startswith('abort'):
      return 'resign'
    if content.lower().startswith('draw'):
      return 'draw'
    content = content[5:]
    try:
      move = board.parse_san(content)
    except chess.InvalidMoveError:
      try:
        move = chess.Move.from_uci(content)
      except:
        move = content
    return move

  async def collect(self, id, board):
    def check(m):
      return m.author.id == id and (m.content.startswith("play ") or m.content.startswith('resign') or m.content.startswith('draw')) and m.channel.id == self.channel.id
    msg = await self.bot.wait_for('message', check=check)
    move = await self.translate_move(msg.content, board)
    while type(move) is str and (move not in ['resign', 'draw'] and move not in board.legal_moves):
      await self.channel.send(f"The move {move} is invalid!")
      msg = await self.bot.wait_for('message', check=check)
      move = await self.translate_move(msg.content, board)
    return move
