from enum import Enum
from pydantic import BaseModel
from typing import List

from common.db import get_client


db = get_client()


class HNodeKind(Enum):
    BP_ENTRY = "H.BPEntry"
    BP_EXIT = "H.BPExit"


class PortSchemaObj(BaseModel):
    slot: int
    name: str
    kind: str
    dataType: str
    mandatory: bool


class NodeSchemaObj(BaseModel):
    name: str
    kind: str
    ingressPorts: List[PortSchemaObj] = []
    egressPorts: List[PortSchemaObj] = []


class NodeSchemaPlugin:

    @classmethod
    def get(cls, kind: str) -> NodeSchemaObj:
        item = db.node_schemata.find_one({"kind": kind})
        # TODO: handle miss
        return NodeSchemaObj(**item)

    @classmethod
    def get_all(cls) -> List[NodeSchemaObj]:
        items = [NodeSchemaObj(**s) for s in db.node_schemata.find({})]
        return items
