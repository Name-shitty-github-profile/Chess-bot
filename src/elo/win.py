from .get import get_elo
from .add import add_elo
def win(loser_id, winner_id):
  loser = get_elo(loser_id)
  winner = get_elo(winner_id)
  difference_w = winner - loser
  difference_l = loser - winner
  del winner, loser
  if difference_w > 500:
    add_elo(winner_id, 50)
  elif difference_w > 200:
    add_elo(winner_id, 25)
  elif 100 < difference_w > -100:
    add_elo(winner_id, 15)
  elif difference_w < -500:
    add_elo(winner_id, 2)
  elif difference_w < -200:
    add_elo(winner_id, 5)
  del difference_w, winner_id
  if difference_l > 500:
    return
  elif difference_l > 200:
    add_elo(loser_id, -2)
  elif 100 < difference_l > -100:
    add_elo(loser_id, -10)
  elif difference_l < -500:
    add_elo(loser_id, -50)
  elif difference_l < -200:
    add_elo(loser_id, -15)

def draw(id1, id2):
  i1 = get_elo(id1)
  i2 = get_elo(id2)
  difference_1 = i1 - i2
  difference_2 = i2 - i1
  del i1, i2
  if difference_1 > 500:
    add_elo(id1, 15)
  elif difference_1 > 200:
    add_elo(id1, 10)
  elif 100 < difference_1 > -100:
    add_elo(id1, 2)
  elif difference_1 < -500:
    add_elo(id1, -15)
  elif difference_1 < -200:
    add_elo(id1, -7)
  del difference_1, id1
  if difference_2 > 500:
    add_elo(id2, 15)
  elif difference_2 > 200:
    add_elo(id2, 10)
  elif 100 < difference_2 > -100:
    add_elo(id2, 2)
  elif difference_2 < -500:
    add_elo(id2, -15)
  elif difference_2 < -200:
    add_elo(id2, -7)
