import pytest

from fastapi.testclient import TestClient
from mongoengine import connect, disconnect

from p1.main import app


@pytest.fixture(scope="class")
def mock_database():
    db = connect("testdb", host="mongomock://localhost")
    yield db
    db.drop_database("testdb")
    db.close()
    disconnect()


@pytest.fixture(scope="class")
def fetch_craftplans(mock_database):
    return client.get(PATH)


@pytest.fixture(scope="class")
def create_craftplan(request, mock_database):
    response = client.post(PATH, json=request.param)
    return response


client = TestClient(app)

PATH = "/craftplans"


@pytest.mark.parametrize(
    "create_craftplan,expected_response",
    [
        ({"name": "ValidName-001", "description": "Some VaLiD description"},
         {"name": "ValidName-001", "description": "Some VaLiD description"}),
        ({"name": "No description provided"},
         {"name": "No description provided",
          "description": "Place for your description"}
         ),
    ],
    indirect=["create_craftplan"]
)
class TestCreateEmptyCraftplan:

    def test_response_is_201(self, create_craftplan, expected_response):
        response = create_craftplan
        assert 201 == response.status_code

    def test_response_has_id(self, create_craftplan, expected_response):
        response = create_craftplan.json()
        assert "id" in response

    def test_valid_response_content(self, create_craftplan, expected_response):
        response = create_craftplan.json()
        response.pop("id")
        assert expected_response == response


@pytest.mark.parametrize(
    "create_craftplan",
    [
        ({"name": "s", "description": "Too short Name"}),
        ({"name": "This name is intentionally set too long"}),
        ({}),
        ({"description": "Forget to set name field"}),
        ({"name": "Too long description", "description": "".zfill(501)}),
    ],
    indirect=["create_craftplan"]
)
class TestFailCraftplanCreateOnInvalidBody:

    def test_response_status_is_422(self, create_craftplan):
        response = create_craftplan
        assert 422 == response.status_code


class TestCraftPlanListEmpty:

    def test_response_status_is_200(self, fetch_craftplans):
        response = fetch_craftplans
        assert 200 == response.status_code

    def test_response_items_are_present(self, fetch_craftplans):
        response = fetch_craftplans.json()
        assert "items" in response

    def test_response_items_content_is_empty(self, fetch_craftplans):
        content = fetch_craftplans.json()
        assert [] == content["items"]
