from pymongo import MongoClient

from common.config import get_config

CONF = get_config()
DB = None


def get_client() -> MongoClient:
    global DB

    if not DB:
        DB = MongoClient(CONF.get("db", "connection"))

    return DB[CONF.get("db", "db_name")]
