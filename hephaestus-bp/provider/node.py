from model.node import NodeDB, NodeDBPlugin


def create_node(kind: str, bp_id: str) -> NodeDB:
    item = NodeDBPlugin.create(kind, bp_id)
    return item
