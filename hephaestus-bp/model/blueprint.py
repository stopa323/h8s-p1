import uuid
from typing import List

from common.db import get_client
from model.node import NodeDB
from provider.node import create_node
from schema.base import HasId
from schema.blueprint import Blueprint
from schema.schemata import HNodeKind

db = get_client()


class BlueprintDB(Blueprint, HasId):
    nodes: List[NodeDB] = []

    @classmethod
    def id_prefix(cls):
        return "bp"


class BlueprintDBPlugin:

    @classmethod
    def create(cls, bp: Blueprint) -> BlueprintDB:
        db_obj = BlueprintDB(**bp.dict())

        ack = db.blueprints.insert_one(db_obj.dict()).acknowledged
        if not ack:
            raise RuntimeError("Could not create blueprint")

        ingress_node = create_node(HNodeKind.BP_ENTRY, db_obj.id)
        egress_node = create_node(HNodeKind.BP_EXIT, db_obj.id)

        db_obj.nodes = [ingress_node, egress_node]

        return db_obj

    @classmethod
    def get_many(cls) -> List[BlueprintDB]:
        items = []
        for bp in db.blueprints.find({}):
            n_docs = db.nodes.find({"blueprint_id": bp["id"]})
            nodes = [NodeDB(**n) for n in n_docs]
            bp["nodes"] = nodes
            items.append(BlueprintDB(**bp))

        return items
