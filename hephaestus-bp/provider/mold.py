from typing import List

from obj.mold import NodeMold, NodeMoldDBPlugin


def get_node_molds() -> List[NodeMold]:
    return NodeMoldDBPlugin.get_all()
