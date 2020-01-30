from model.node import NodeDB, NodeDBPlugin
from schema.schemata import HNodeKind


def create_node(kind: HNodeKind, bp_id: str) -> NodeDB:
    item = NodeDBPlugin.create(kind, bp_id)
    return item
