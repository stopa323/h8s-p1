import logging
import yaml
from pymongo import MongoClient

from common.config import get_config
from schema import schemata


LOG = logging.getLogger(__name__)

CONF = get_config()
DB = None


def get_client() -> MongoClient:
    global DB

    if not DB:
        DB = MongoClient(CONF.get("db", "connection"))

    return DB[CONF.get("db", "db_name")]


def load_core_schemata():
    LOG.info("Load core schemata")

    path = CONF.get("schemata", "core")
    with open(path) as f:
        data = yaml.safe_load(f)

    nodes = data.get("nodes")
    if not nodes:
        LOG.error(f"Missing or empty `nodes` section in {path} file")
        raise ValueError("Unable to load core schemata")

    if type(nodes) is not dict:
        LOG.error(f"Expected dict in `nodes` section but {type(nodes)} found")
        raise ValueError("Unable to load core schemata")

    db = get_client()
    for _id, node in nodes.items():
        item = schemata.NodeSchemata(**node)
        db.node_schemata.update({"kind": item.kind}, item.dict(), upsert=True)