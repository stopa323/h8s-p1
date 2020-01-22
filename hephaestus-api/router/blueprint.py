from fastapi import APIRouter

from provider import blueprint
from schema import Blueprint, BlueprintCreate


router = APIRouter()


@router.post("/", response_model=Blueprint)
async def create_blueprint(bp: BlueprintCreate) -> Blueprint:
    item = blueprint.create_blueprint(bp)
    return item
