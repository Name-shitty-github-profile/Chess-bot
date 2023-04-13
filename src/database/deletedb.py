from .client import gt
def delete(id: int, collection: str) -> None:
  db = gt(collection)
  db.delete_one({"_id": id})
  return None
