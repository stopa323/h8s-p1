from fastapi import APIRouter
from typing import List

from provider import blueprint
from model.blueprint import BlueprintCreate, BlueprintObj


router = APIRouter()


@router.post("/blueprints", response_model=BlueprintObj)
async def create_blueprint(bp: BlueprintCreate):
    item = blueprint.create_blueprint(bp)
    return item


@router.get("/blueprints", response_model=List[BlueprintObj])
async def get_blueprint_list():
    items = blueprint.get_blueprint_list()
    return items
