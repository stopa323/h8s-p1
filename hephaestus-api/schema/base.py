from pydantic import BaseModel
from uuid import UUID


class HasId(BaseModel):
    id: UUID

    def __init__(self, **data):
        if "_id" in data:
            data["id"] = data["_id"]
            del data["_id"]
        super(HasId, self).__init__(**data)
