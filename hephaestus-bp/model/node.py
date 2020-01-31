from common.db import get_client
from provider.schemata import NodeSchemataDBPlugin
from schema import schemata
from model import base

db = get_client()


class NodeDB(base.HasId, schemata.NodeSchemata):
    blueprint_id: str

    @classmethod
    def id_prefix(cls):
        return "node"


class NodeDBPlugin:

    @classmethod
    def create(cls, kind: schemata.HNodeKind, bp_id: str) -> NodeDB:
        schema = NodeSchemataDBPlugin.get(kind)

        data = schema.dict()
        data["blueprint_id"] = bp_id

        node = NodeDB(**data)
        ack = db.nodes.insert_one(node.dict()).acknowledged
        if not ack:
            raise RuntimeError(f"Could not create {kind} node")

        return node
