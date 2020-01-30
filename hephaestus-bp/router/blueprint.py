from fastapi import APIRouter
from typing import List

from provider import blueprint
from schema.blueprint import Blueprint
from model.blueprint import BlueprintDB


router = APIRouter()


@router.post("/blueprints", response_model=BlueprintDB)
async def create_blueprint(bp: Blueprint):
    item = blueprint.create_blueprint(bp)
    return item


@router.get("/blueprints", response_model=List[BlueprintDB])
async def get_blueprint_list():
    items = blueprint.get_blueprint_list()
    return items
