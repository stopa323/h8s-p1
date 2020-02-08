from pydantic import BaseModel

from common.db import get_client
from model.base import HasId
from provider.blueprint import get_blueprint

db = get_client()


class LinkRivet(BaseModel):
    node_id: str
    slot: int


class LinkCreate(BaseModel):
    source: LinkRivet
    sink: LinkRivet


class LinkObj(LinkCreate, HasId):
    blueprint_id: str

    @classmethod
    def id_prefix(cls):
        return "link"


class LinkPlugin:

    @classmethod
    def create(cls, link: LinkCreate, blueprint_id: str) -> LinkObj:
        bp = get_blueprint(blueprint_id)
        data = link.dict()
        data["blueprint_id"] = bp.id

        # TODO: Data type validation must be performed here

        db_obj = LinkObj(**data)
        ack = db.links.insert_one(db_obj.dict()).acknowledged
        if not ack:
            raise RuntimeError("Could not create link")

        return db_obj
