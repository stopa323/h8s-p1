from common.db import get_client
from provider.schema import NodeSchemaPlugin
from model import base, schema

db = get_client()


class NodeDB(base.HasId, schema.NodeSchemaObj):
    blueprint_id: str

    @classmethod
    def id_prefix(cls):
        return "node"


class NodeDBPlugin:

    @classmethod
    def create(cls, kind: str, bp_id: str) -> NodeDB:
        schema = NodeSchemaPlugin.get(kind)

        data = schema.dict()
        data["blueprint_id"] = bp_id

        node = NodeDB(**data)
        ack = db.nodes.insert_one(node.dict()).acknowledged
        if not ack:
            raise RuntimeError(f"Could not create {kind} node")

        return node
