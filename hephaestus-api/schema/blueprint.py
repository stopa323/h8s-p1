from pydantic import BaseModel
from uuid import uuid4, UUID

from common.db import get_client


db = get_client()


class HasId(BaseModel):
    id: UUID

    def __init__(self, **data):
        if "_id" in data:
            data["id"] = data["_id"]
            del data["_id"]
        super(HasId, self).__init__(**data)


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
