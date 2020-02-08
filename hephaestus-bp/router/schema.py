from fastapi import APIRouter
from typing import List

from provider import schema
from obj.schema import NodeSchemaObj


router = APIRouter()


@router.get("/schema/nodes",
            response_model=List[NodeSchemaObj])
async def get_nodes_schemata():
    items = schema.get_nodes_schemata()
    return items
