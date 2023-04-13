from .client import gt
def search(id: int, collection: str) -> dict:
  db = gt(collection)
  return db.find_one({"_id": id})
