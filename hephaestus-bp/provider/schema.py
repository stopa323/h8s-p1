from typing import List

from model.schema import NodeSchemaObj, NodeSchemaPlugin


def get_nodes_schemata() -> List[NodeSchemaObj]:
    return NodeSchemaPlugin.get_all()
