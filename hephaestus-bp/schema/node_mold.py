from typing import Optional, List
from schema.base import HasId


class NodeMoldBase(HasId):
    name: str
    kind: str
    tags: Optional[List[str]]
