import uuid
from pydantic import BaseModel


class HasId(BaseModel):
    id: str

    def __init__(self, **data):
        if "id" not in data:
            data["id"] = self.generate_id()

        super(HasId, self).__init__(**data)

    @classmethod
    def id_prefix(cls) -> str:
        return "obj"

    def generate_id(self) -> str:
        prefix = self.id_prefix()
        _id = str(uuid.uuid4())[-12:]
        return f"{prefix}-{_id}"
