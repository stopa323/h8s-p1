import pytest

from mongoengine import connect, disconnect

from p1.db import craftplan as db
from p1.provider import craftplan as provider
from p1.schema import craftplan as schema


@pytest.fixture(scope="class")
def mock_database():
    db = connect("testdb", host="mongomock://localhost")
    yield db
    db.drop_database("testdb")
    db.close()
    disconnect()


@pytest.fixture(scope="class")
def create_craftplan(mock_database):
    cp = schema.CraftPlanCreate(name="cp1", description="desc1")
    cp_db = provider.create_craftplan(cp)
    return cp_db


class TestCreateEmptyCraftplan:

    def test_craftplan_saved_in_db(self, create_craftplan):
        assert 1 == len(list(db.CraftPlanObj.objects))

    def test_db_id_matches_response_id(self, create_craftplan):
        cp_db = create_craftplan
        assert cp_db.id == db.CraftPlanObj.objects[0].id

    def test_response_has_valid_name(self, create_craftplan):
        cp_db = create_craftplan
        assert "cp1" == cp_db.name

    def test_response_has_valid_description(self, create_craftplan):
        cp_db = create_craftplan
        assert "desc1" == cp_db.description

    def test_craftplan_created_with_no_nodes(self, create_craftplan):
        cp_db = create_craftplan
        assert [] == cp_db.nodes


def test_default_craftplan_description(mock_database):
    cp = schema.CraftPlanCreate(name="cp1")
    cp_db = provider.create_craftplan(cp)
    assert "Place for your description" == cp_db.description


def test_craftplan_is_deleted_from_db(mock_database):
    cp1 = db.CraftPlanObj(name="cp1")
    cp1.save()
    cp2 = db.CraftPlanObj(name="cp2")
    cp2.save()

    provider.delete_craftplan(cp1.id)

    assert 1 == len(db.CraftPlanObj.objects)
    assert cp2 == db.CraftPlanObj.objects[0]
