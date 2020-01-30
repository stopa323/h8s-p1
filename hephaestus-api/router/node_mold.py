from fastapi import APIRouter
from typing import List

from provider import node_mold


router = APIRouter()


@router.get("/nodes",
            response_model=List[str],
            response_model_exclude={"id"})
async def get_node_molds():
    items = node_mold.get_molds()
    return items
