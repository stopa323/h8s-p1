from fastapi import APIRouter
from typing import List

from provider import blueprint, link as link_provider
from model.blueprint import BlueprintCreate, BlueprintObj
from model.link import LinkCreate, LinkObj
from model.node import NodeDB


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


@router.post("/blueprints/{blueprint_id}/nodes",
             response_model=NodeDB,
             name="Add node to blueprint",
             description="Creates new node inside blueprint document")
async def add_node(node_kind: str, blueprint_id: str):
    item = blueprint.add_node(node_kind, blueprint_id)
    return item


@router.post("/blueprints/{blueprint_id}/links",
             response_model=LinkObj,
             name="Add link to blueprint",
             description="Creates link between two nodes")
async def add_link(link: LinkCreate, blueprint_id: str):
    item = link_provider.create_link(link, blueprint_id)
    return item
