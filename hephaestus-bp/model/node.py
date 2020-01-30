import uuid

from common.db import get_client
from provider.schemata import NodeSchemataDBPlugin
from schema import base, schemata


db = get_client()


class NodeDB(base.HasId, schemata.NodeSchemata):
    blueprint_id: uuid.UUID


class NodeDBPlugin:

    @classmethod
    def create(cls, kind: schemata.HNodeKind, bp_id: str) -> NodeDB:
        schema = NodeSchemataDBPlugin.get(kind)

        data = schema.dict()
        data["blueprint_id"] = bp_id

        node = NodeDB(**data)
        db.nodes.insert_one(node.dict())

        return node
