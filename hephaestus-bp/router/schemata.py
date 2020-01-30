from fastapi import APIRouter
from typing import List

from provider import schemata
from schema.schemata import NodeSchemata


router = APIRouter()


@router.get("/schemata/nodes",
            response_model=List[NodeSchemata])
async def get_nodes_schemata():
    items = schemata.get_nodes_schemata()
    return items
