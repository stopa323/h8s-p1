from typing import List

from common.db import get_client
from schema import Blueprint, BlueprintCreate


db = get_client()


def create_blueprint(bp: BlueprintCreate) -> Blueprint:
    data = bp.save()
    item = Blueprint(**data)
    return item


def get_blueprint_list() -> List[Blueprint]:
    items = list()
    for bp in db.blueprints.find({}):
        bp["id"] = bp["_id"]
        items.append(Blueprint(**bp))

    return items