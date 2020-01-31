import logging
import yaml

from common.config import get_config
from common.db import get_client
from model import schema


CONF = get_config()
LOG = logging.getLogger(__name__)


def set_up_indexes():
    db = get_client()
    db.blueprints.create_index("id", unique=True)
    db.nodes.create_index("id", unique=True)
    db.node_schemata.create_index("kind", unique=True)


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
        item = schema.NodeSchemaObj(**node)
        db.node_schemata.update({"kind": item.kind}, item.dict(), upsert=True)