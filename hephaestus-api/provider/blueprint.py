from common.db import get_client
from schema import Blueprint, BlueprintCreate


db = get_client()


def create_blueprint(bp: BlueprintCreate) -> Blueprint:
    data = bp.save()
    item = Blueprint(**data)
    return item
