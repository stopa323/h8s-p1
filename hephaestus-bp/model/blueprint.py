from pydantic import BaseModel, Field
from typing import List

from common.db import get_client
from model.node import NodeDB
from provider.node import create_node
from model.base import HasId
from model.link import LinkObj
from model.schema import HNodeKind

db = get_client()


class BlueprintCreate(BaseModel):
    name: str = Field(..., description="Name of the blueprint", min_length=1,
                      max_length=50)


class BlueprintObj(BlueprintCreate, HasId):
    nodes: List[NodeDB] = []
    links: List[LinkObj] = []

    @classmethod
    def id_prefix(cls):
        return "bp"


class BlueprintPlugin:

    @classmethod
    def create(cls, bp: BlueprintCreate) -> BlueprintObj:
        db_obj = BlueprintObj(**bp.dict())

        ack = db.blueprints.insert_one(db_obj.dict()).acknowledged
        if not ack:
            raise RuntimeError("Could not create blueprint")

        ingress_node = create_node(HNodeKind.BP_ENTRY.value, db_obj.id)
        egress_node = create_node(HNodeKind.BP_EXIT.value, db_obj.id)

        db_obj.nodes = [ingress_node, egress_node]

        return db_obj

    @classmethod
    def get_many(cls) -> List[BlueprintObj]:
        items = []
        for bp in db.blueprints.find({}):
            n_docs = db.nodes.find({"blueprint_id": bp["id"]})
            nodes = [NodeDB(**n) for n in n_docs]
            bp["nodes"] = nodes
            items.append(BlueprintObj(**bp))

        return items
