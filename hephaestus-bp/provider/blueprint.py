from typing import List

from model.blueprint import BlueprintCreate, BlueprintObj, BlueprintPlugin
from model.node import NodeDB, NodeDBPlugin


def create_blueprint(bp: BlueprintCreate) -> BlueprintObj:
    item = BlueprintPlugin.create(bp)
    return item


def get_blueprint_list() -> List[BlueprintObj]:
    items = BlueprintPlugin.get_many()
    return items


def get_blueprint(_id: str) -> BlueprintObj:
    pass


def add_node(node_kind: str, blueprint_id: str) -> NodeDB:
    node = NodeDBPlugin.create(node_kind, blueprint_id)
    return node
