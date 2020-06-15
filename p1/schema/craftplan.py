from typing import List
from pydantic import BaseModel, Field


class CraftPlanCreate(BaseModel):
    name: str = Field(...,
                      title="Name your craftplan",
                      min_length=3, max_length=32)
    description: str = Field("Place for your description",
                             title="Describe your craftplan briefly",
                             max_length=500)

    class Config:
        orm_mode = True

        schema_extra = {
            "description": "Object for creating Craftplan",
            "example": {
                "name": "My First Craftplan",
                "description": "Deploy some infra"}}


class CraftPlan(CraftPlanCreate):
    id: str = Field(...,
                    title="Unique resource Id")

    class Config:
        orm_mode = True

        schema_extra = {
            "description": "Craftplan object",
            "example": {
                "id": "00000000-0000-0000-0000-000000000001",
                "name": "My First Craftplan",
                "description": "Deploy some infra"}}


class CraftPlanList(BaseModel):
    items: List[CraftPlan] = Field(...,
                                   title="List of available Craftplans")
