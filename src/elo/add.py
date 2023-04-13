from .get import get_elo
from database import add
def add_elo(id, number):
  current = get_elo(id)
  current += number
  add({"_id": id, 'elo': current}, 'elo')
