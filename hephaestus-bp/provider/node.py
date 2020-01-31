from model.node import NodeDB, NodeDBPlugin
from model.schema import HNodeKind


def create_node(kind: HNodeKind, bp_id: str) -> NodeDB:
    item = NodeDBPlugin.create(kind, bp_id)
    return item
