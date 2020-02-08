from typing import List

from obj.schema import NodeSchemaObj, NodeSchemaPlugin


def get_nodes_schemata() -> List[NodeSchemaObj]:
    return NodeSchemaPlugin.get_all()
