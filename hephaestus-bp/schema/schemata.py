from pydantic import BaseModel
from typing import List


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
