from fastapi import APIRouter
from typing import List

from provider import blueprint
from model.blueprint import BlueprintCreate, BlueprintObj


router = APIRouter()


@router.post("/blueprints",
             response_model=BlueprintObj,
             name="Create new blueprint",
             description="Initialize new blueprint document. Always create with"
                         " entry and exit nodes")
async def create_blueprint(bp: BlueprintCreate):
    item = blueprint.create_blueprint(bp)
    return item


@router.get("/blueprints",
            response_model=List[BlueprintObj],
            name="Get blueprint documents",
            description="Fetch all defined blueprint documents.")
async def get_blueprint_list():
    items = blueprint.get_blueprint_list()
    return items
