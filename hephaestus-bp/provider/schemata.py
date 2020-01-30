from typing import List

from common.db import get_client
from schema.schemata import NodeSchemata


db = get_client()


def get_nodes_schemata() -> List[NodeSchemata]:
    items = [NodeSchemata(**s) for s in db.node_schemata.find({})]
    return items
