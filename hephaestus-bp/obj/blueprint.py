from pydantic import BaseModel, Field
from typing import List

from common.db import get_client
from obj.base import HasId
from obj.schema import NodeSchemaObj
from provider.schema import NodeSchemaPlugin

db = get_client()


class Node(HasId, NodeSchemaObj):
    blueprint_id: str

    @classmethod
    def id_prefix(cls):
        return "node"


class LinkRivet(BaseModel):
    node_id: str
    slot: int


class LinkCreate(BaseModel):
    source: LinkRivet
    sink: LinkRivet


class Link(LinkCreate, HasId):
    blueprint_id: str

    @classmethod
    def id_prefix(cls):
        return "link"


class BlueprintCreate(BaseModel):
    name: str = Field(..., description="Name of the blueprint", min_length=1,
                      max_length=50)


class Blueprint(BlueprintCreate, HasId):
    nodes: List[Node] = []
    links: List[Link] = []

    @classmethod
    def id_prefix(cls):
        return "bp"


class NodeDBPlugin:

    @classmethod
    def create(cls, kind: str, bp_id: str) -> Node:
        node_schema = NodeSchemaPlugin.get(kind)

        data = node_schema.dict()
        data["blueprint_id"] = bp_id

        node = Node(**data)
        ack = db.nodes.insert_one(node.dict()).acknowledged
        if not ack:
            raise RuntimeError(f"Could not create {kind} node")

        return node

    @classmethod
    def delete(cls, blueprint_id: str, node_id: str):
        res = db.nodes.delete_one({"id": node_id, "blueprint_id": blueprint_id})
        if 0 == res.deleted_count:
            raise RuntimeError(f"Could not find Node {node_id} within Blueprint"
                               f" {blueprint_id}")


class LinkDBPlugin:

    @classmethod
    def create(cls, link: LinkCreate, blueprint_id: str) -> Link:
        data = link.dict()
        data["blueprint_id"] = blueprint_id

        # TODO: Data type validation must be performed here

        db_obj = Link(**data)
        ack = db.links.insert_one(db_obj.dict()).acknowledged
        if not ack:
            raise RuntimeError("Could not create link")

        return db_obj

    @classmethod
    def delete(cls, blueprint_id: str, link_id: str):
        res = db.links.delete_one({"id": link_id, "blueprint_id": blueprint_id})
        if 0 == res.deleted_count:
            raise RuntimeError(f"Could not find Link {link_id} within Blueprint"
                               f" {blueprint_id}")

    @classmethod
    def delete_by_node(cls, blueprint_id: str, node_id: str):
        """Deletes all links associated with particular node."""
        query = {"$and": [
            {"blueprint_id": blueprint_id},
            {"$or": [
                {"sink.node_id": node_id},
                {"source.node_id": node_id}]}]}
        res = db.links.delete_many(query)
        return res


class BlueprintDBPlugin:

    @classmethod
    def create(cls, bp: BlueprintCreate) -> Blueprint:
        db_obj = Blueprint(**bp.dict())

        ack = db.blueprints.insert_one(db_obj.dict()).acknowledged
        if not ack:
            raise RuntimeError("Could not create blueprint")

        return db_obj

    @classmethod
    def get_many(cls) -> List[Blueprint]:
        items = []
        for bp in db.blueprints.find({}):
            cls._fetch_sub_objects(bp)
            items.append(Blueprint(**bp))

        return items

    @classmethod
    def get(cls, _id: str) -> Blueprint:
        bp = db.blueprints.find_one({"id": _id})
        if not bp:
            raise RuntimeError(f"Blueprint {_id} not found")

        cls._fetch_sub_objects(bp)

        return Blueprint(**bp)

    @classmethod
    def _fetch_sub_objects(cls, bp: dict):
        """Populates blueprint dict with link & node sub-resources."""
        # Fetch associated nodes
        n_docs = db.nodes.find({"blueprint_id": bp["id"]})
        nodes = [Node(**n) for n in n_docs]
        bp["nodes"] = nodes

        # Fetch associated links
        l_docs = db.links.find({"blueprint_id": bp["id"]})
        links = [Link(**n) for n in l_docs]
        bp["links"] = links
