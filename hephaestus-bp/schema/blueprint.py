from pydantic import BaseModel


class Blueprint(BaseModel):
    name: str
