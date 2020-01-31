from typing import List

from model.blueprint import BlueprintCreate, BlueprintObj, BlueprintPlugin


def create_blueprint(bp: BlueprintCreate) -> BlueprintObj:
    item = BlueprintPlugin.create(bp)
    return item


def get_blueprint_list() -> List[BlueprintObj]:
    items = BlueprintPlugin.get_many()
    return items
