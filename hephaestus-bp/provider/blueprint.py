from typing import List

import obj


def get_blueprint(_id: str) -> obj.Blueprint:
    item = obj.BlueprintDBPlugin.get(_id)
    return item


def get_blueprint_many() -> List[obj.Blueprint]:
    items = obj.BlueprintDBPlugin.get_many()
    return items


def create_blueprint(bp: obj.BlueprintCreate) -> obj.Blueprint:
    blueprint = obj.BlueprintDBPlugin.create(bp)

    # Create blueprint ingress/egress
    ingress = obj.NodeDBPlugin.create(obj.HNodeKind.BP_ENTRY.value,
                                      blueprint.id)
    egress = obj.NodeDBPlugin.create(obj.HNodeKind.BP_EXIT.value, blueprint.id)
    blueprint.nodes = [ingress, egress]

    # Link nodes together with execution flow
    data = {"source": {"node_id": ingress.id, "slot": 0},
            "sink": {"node_id": egress.id, "slot": 0}}
    lc = obj.LinkCreate(**data)
    flow_link = obj.LinkDBPlugin.create(lc, blueprint.id)
    blueprint.links = [flow_link]

    return blueprint


def add_node(node_kind: str, blueprint_id: str) -> obj.Node:
    bp = obj.BlueprintDBPlugin.get(blueprint_id)
    node = obj.NodeDBPlugin.create(node_kind, bp.id)
    return node


def delete_node(blueprint_id: str, node_id: str):
    obj.NodeDBPlugin.delete(blueprint_id, node_id)
    obj.LinkDBPlugin.delete_by_node(blueprint_id, node_id)


def add_link(link: obj.LinkCreate, blueprint_id: str) -> obj.Link:
    bp = obj.BlueprintDBPlugin.get(blueprint_id)
    link_obj = obj.LinkDBPlugin.create(link, bp.id)
    return link_obj


def delete_link(blueprint_id: str, link_id: str):
    obj.LinkDBPlugin.delete(blueprint_id, link_id)
