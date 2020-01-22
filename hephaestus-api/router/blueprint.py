from fastapi import APIRouter
from typing import List

from provider import blueprint
from schema import Blueprint, BlueprintCreate


router = APIRouter()


@router.post("/", response_model=Blueprint)
async def create_blueprint(bp: BlueprintCreate):
    item = blueprint.create_blueprint(bp)
    return item


@router.get("/", response_model=List[Blueprint])
async def get_blueprint_list():
    items = blueprint.get_blueprint_list()
    return items
