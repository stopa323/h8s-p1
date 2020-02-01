import logging
import os
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


def load_schema_file(path: str) -> bool:
    with open(path) as f:
        data = yaml.safe_load(f)

    nodes = data.get("nodes")
    if not nodes:
        LOG.error(f"Skipping ({path}) - missing or empty `nodes` section")
        return False

    if type(nodes) is not dict:
        LOG.error(f"Skipping ({path}) - expected dict in `nodes` section but "
                  f"{type(nodes)} found")
        return False

    db = get_client()
    for _id, node in nodes.items():
        item = schema.NodeSchemaObj(**node)
        db.node_schemata.update({"kind": item.kind}, item.dict(), upsert=True)

    return True


def load_schemas() -> None:
    schema_dir = CONF.get("schemata", "dir")
    LOG.info(f"Scanning schema directory ({schema_dir}) for new schemas...")
    schema_paths = []
    for root, dirs, files in os.walk(schema_dir):
        for f in files:
            schema_paths.append(os.path.join(root, f))

    for path in schema_paths:
        if load_schema_file(path):
            LOG.info(f"Loaded: {path}")
