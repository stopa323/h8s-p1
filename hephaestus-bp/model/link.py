from pydantic import BaseModel

from model.base import HasId


class LinkCreate(BaseModel):
    pass


class LinkObj(LinkCreate, HasId):
    pass
