from pydantic import BaseModel
from uuid import uuid4

from common.db import get_client
from schema.base import HasId


db = get_client()


class BlueprintCreate(BaseModel):
    name: str

    def save(self) -> dict:
        """Save model in database."""
        data = self.dict()
        data["_id"] = uuid4()

        _id = db.blueprints.insert_one(data).inserted_id
        data["id"] = _id
        del data["_id"]

        return data


class Blueprint(HasId, BlueprintCreate):
    pass
