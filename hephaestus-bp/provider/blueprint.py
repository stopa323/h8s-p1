from typing import List

from model.blueprint import BlueprintDB, BlueprintDBPlugin
from schema.blueprint import Blueprint


def create_blueprint(bp: Blueprint) -> BlueprintDB:
    item = BlueprintDBPlugin.create(bp)
    return item


def get_blueprint_list() -> List[BlueprintDB]:
    items = BlueprintDBPlugin.get_many()
    return items
