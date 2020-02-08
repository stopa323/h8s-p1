from fastapi import APIRouter
from typing import List

import obj
from provider import blueprint


router = APIRouter()


@router.get("/blueprints/{blueprint_id}",
            response_model=obj.Blueprint,
            name="Get blueprint document",
            description="Fetch blueprint document.")
async def get_blueprint(blueprint_id: str):
    item = blueprint.get_blueprint(blueprint_id)
    return item


@router.get("/blueprints",
            response_model=List[obj.Blueprint],
            name="Get blueprint documents",
            description="Fetch all defined blueprint documents.")
async def get_blueprint_many():
    items = blueprint.get_blueprint_many()
    return items


@router.post("/blueprints",
             response_model=obj.Blueprint,
             name="Create new blueprint",
             description="Initialize new blueprint document. Always create with"
                         " entry and exit nodes")
async def create_blueprint(bp: obj.BlueprintCreate):
    item = blueprint.create_blueprint(bp)
    return item


@router.post("/blueprints/{blueprint_id}/nodes",
             response_model=obj.Node,
             name="Add node to blueprint",
             description="Creates new node inside blueprint document")
async def add_node(node_kind: str, blueprint_id: str):
    item = blueprint.add_node(node_kind, blueprint_id)
    return item


@router.delete("/blueprints/{blueprint_id}/nodes/{node_id}",
               name="Remove node from blueprint",
               description="Removes node and associated links from blueprint")
async def delete_link(blueprint_id: str, node_id: str):
    blueprint.delete_node(blueprint_id, node_id)
    return {}


@router.post("/blueprints/{blueprint_id}/links",
             response_model=obj.Link,
             name="Add link to blueprint",
             description="Creates link between two nodes")
async def add_link(link: obj.LinkCreate, blueprint_id: str):
    item = blueprint.add_link(link, blueprint_id)
    return item


@router.delete("/blueprints/{blueprint_id}/links/{link_id}",
               name="Remove link from blueprint",
               description="Removes link between two nodes")
async def delete_link(blueprint_id: str, link_id: str):
    blueprint.delete_link(blueprint_id, link_id)
    return {}
