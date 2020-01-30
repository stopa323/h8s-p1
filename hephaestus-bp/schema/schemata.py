from enum import Enum
from pydantic import BaseModel
from typing import List


class HNodeKind(Enum):
    BP_ENTRY = "H.BPEntry"
    BP_EXIT = "H.BPExit"


class PortSchemata(BaseModel):
    name: str
    kind: str
    dataType: str
    mandatory: bool


class NodeSchemata(BaseModel):
    name: str
    kind: str
    ingressPorts: List[PortSchemata] = []
    egressPorts: List[PortSchemata] = []
