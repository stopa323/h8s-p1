# type: ignore
from fastapi import APIRouter

from p1.provider import craftplan as provider
from p1.schema import craftplan as api


router = APIRouter()


@router.get("/craftplans",
            name="List Craftplans",
            description="Fetch list of all saved craftplans",
            response_model=api.CraftPlanList,
            tags=["Craftplan"])
async def list_pancakes():
    objects = provider.list_craftplans()
    return {"items": objects}


@router.post("/craftplans",
             name="Create Craftplan",
             description="Create new Craftplan document",
             response_model=api.CraftPlan,
             status_code=201,
             tags=["Craftplan"])
async def create_craftplan(craftplan: api.CraftPlanCreate):
    object = provider.create_craftplan(craftplan)
    return object
