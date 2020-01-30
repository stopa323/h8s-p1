import uuid
from pydantic import BaseModel


class HasId(BaseModel):
    id: uuid.UUID

    def __init__(self, **data):
        # ID from database
        if "_id" in data:
            data["id"] = data["_id"]
            del data["_id"]
        # Generate ID for object
        elif "id" not in data:
            data["id"] = uuid.uuid4()

        super(HasId, self).__init__(**data)
