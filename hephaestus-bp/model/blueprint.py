import uuid
from typing import List

from common.db import get_client
from model.node import HNodeKind, NodeDB
from provider.node import create_node
from schema.base import HasId
from schema.blueprint import Blueprint

db = get_client()


class BlueprintDB(Blueprint, HasId):
    nodes: List[NodeDB] = []


class BlueprintDBPlugin:

    @classmethod
    def create(cls, bp: Blueprint) -> BlueprintDB:
        data = bp.dict()
        data["_id"] = uuid.uuid4()

        bp_id = db.blueprints.insert_one(data).inserted_id
        data["id"] = bp_id

        ingress_node = create_node(HNodeKind.BP_INGRESS, bp_id)
        egress_node = create_node(HNodeKind.BP_EGRESS, bp_id)

        data["nodes"] = [ingress_node, egress_node]

        return BlueprintDB(**data)

    @classmethod
    def get_many(cls) -> List[BlueprintDB]:
        items = []
        for bp in db.blueprints.find({}):
            n_docs = db.nodes.find({"blueprint_id": bp["_id"]})
            nodes = [NodeDB(**n) for n in n_docs]
            bp["nodes"] = nodes
            items.append(BlueprintDB(**bp))

        return items
