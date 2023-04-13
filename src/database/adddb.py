from .client import gt
def add(data: dict, collection: str) -> None:
  db = gt(collection)
  try:
    db.insert_one(data)
  except:
    db.update_one({'_id': data['_id']}, {'$set': data})
  return None
