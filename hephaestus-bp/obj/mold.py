from enum import Enum
from pydantic import BaseModel
from typing import List

from common.db import get_client


db = get_client()


class HNodeKind(Enum):
    BP_ENTRY = "H.BPEntry"
    BP_EXIT = "H.BPExit"


class PortMold(BaseModel):
    slot: int
    name: str
    kind: str
    dataType: str
    mandatory: bool


class NodeMold(BaseModel):
    name: str
    kind: str
    ingressPorts: List[PortMold] = []
    egressPorts: List[PortMold] = []


class NodeMoldDBPlugin:

    @classmethod
    def get(cls, kind: str) -> NodeMold:
        item = db.node_schemata.find_one({"kind": kind})
        # TODO: handle miss
        return NodeMold(**item)

    @classmethod
    def get_all(cls) -> List[NodeMold]:
        items = [NodeMold(**s) for s in db.node_schemata.find({})]
        return items
