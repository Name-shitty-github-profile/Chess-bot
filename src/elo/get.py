from database import search, add
def get_elo(id) -> int:
  try:
    return search(id, 'elo')['elo']
  except:
    add({"_id": id, 'elo': 1000}, 'elo')
    return 1000
