import pytest

from mongoengine import connect, disconnect

from p1.db import craftplan as db
from p1.provider import craftplan as provider
from p1.schema import craftplan as schema


@pytest.fixture(scope="function")
def db_mock():
    db = connect("testdb", host="mongomock://localhost")
    yield db
    db.drop_database("testdb")
    db.close()
    disconnect()


def test_create_empty_craftplan(db_mock):
    cp = schema.CraftPlanCreate(name="cp1", description="desc1")

    cp_db = provider.create_craftplan(cp)

    assert 1 == len(list(db.CraftPlanObj.objects)), "Obj not saved in DB"
    assert cp_db.id == db.CraftPlanObj.objects[0].id
    assert "cp1" == cp_db.name
    assert "desc1" == cp_db.description
    assert [] == cp_db.nodes


def test_default_craftplan_description(db_mock):
    cp = schema.CraftPlanCreate(name="cp1")

    cp_db = provider.create_craftplan(cp)

    assert "Place for your description" == cp_db.description
