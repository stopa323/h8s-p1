from fastapi import APIRouter
from typing import List

from provider import mold
from obj.mold import NodeMold


router = APIRouter()


@router.get("/molds/nodes",
            response_model=List[NodeMold])
async def get_node_molds():
    items = mold.get_node_molds()
    return items
