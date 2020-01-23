from typing import List

from common.db import get_client
from schema.node_mold import NodeMoldBase


db = get_client()


def get_molds() -> List[NodeMoldBase]:
    items = [NodeMoldBase(**mold) for mold in db.molds.find({})]
    return items
