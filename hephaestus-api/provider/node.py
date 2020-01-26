from model.node import HNodeKind, NodeDB, NodeDBPlugin


def create_node(kind: HNodeKind, bp_id: str) -> NodeDB:
    item = NodeDBPlugin.create(kind, bp_id)
    return item
