import chess.svg
from .image import svg_png
import nextcord, random, os
class Sending:
  def __init__(self, channel):
    self.file = f"pics/{(no := random.randint(00000000000000, 9999999999999999999))}.png"
    self.fsvg = f'svg/{no}.txt'
    for i in [self.file, self.fsvg]:
      with open(i, 'x') as f:
        f.write('Yes.')
    self.channel = channel

  async def send(self, text, board, color):
    with open(self.fsvg, 'w') as f:
      f.write(str(chess.svg.board(board, size=350, orientation=color)))
    svg_png(self.fsvg, self.file)
    await self.channel.send(text, file=nextcord.File(self.file))

  def end(self):
    os.remove(self.file)
    os.remove(self.fsvg)
