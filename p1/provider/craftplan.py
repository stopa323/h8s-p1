from typing import List

from p1.db import craftplan as db
from p1.schema import craftplan as api


def list_craftplans() -> List[db.CraftPlanObj]:
    db_objects = db.CraftPlanObj.objects
    return list(db_objects)


def create_craftplan(craftplan: api.CraftPlanCreate) -> db.CraftPlanObj:
    craftplan_db = db.CraftPlanObj(**craftplan.dict())
    craftplan_db.save()
    return craftplan_db
