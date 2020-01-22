from pydantic import BaseModel, Field
from uuid import uuid4, UUID

from common.db import get_client


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


class Blueprint(BlueprintCreate):
    id: UUID
