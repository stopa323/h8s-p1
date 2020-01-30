from pydantic import BaseModel
from typing import List


class PortSchemata(BaseModel):
    name: str
    kind: str
    dataType: str


class NodeSchemata(BaseModel):
    name: str
    kind: str
    ingressPorts: List[PortSchemata] = []
    egressPorts: List[PortSchemata] = []
