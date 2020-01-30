from typing import List

from common.db import get_client
from schema.schemata import HNodeKind, NodeSchemata


db = get_client()


def get_nodes_schemata() -> List[NodeSchemata]:
    return NodeSchemataDBPlugin.get_all()


class NodeSchemataDBPlugin:

    @classmethod
    def get(cls, kind: HNodeKind) -> NodeSchemata:
        item = db.node_schemata.find_one({"kind": kind.value})
        return NodeSchemata(**item)

    @classmethod
    def get_all(cls) -> List[NodeSchemata]:
        items = [NodeSchemata(**s) for s in db.node_schemata.find({})]
        return items
