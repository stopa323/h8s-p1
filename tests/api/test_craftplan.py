import pytest

from fastapi.testclient import TestClient
from mongoengine import connect, disconnect

from p1.main import app


@pytest.fixture(scope="function")
def db_mock():
    db = connect("testdb", host="mongomock://localhost")
    yield db
    db.drop_database("testdb")
    db.close()
    disconnect()


client = TestClient(app)

CREATE_PATH = "/craftplans"


@pytest.mark.parametrize(
    "body,expected_response",
    [
        (
            {"name": "ValidName-001",
             "description": "Some VaLiD description"},
            {"name": "ValidName-001",
             "description": "Some VaLiD description"}),
        (
            {"name": "No description provided"},
            {"name": "No description provided",
             "description": "Place for your description"}),
    ]
)
def test_create_craftplan_success(
        body, expected_response, db_mock):
    response = client.post(CREATE_PATH, json=body)

    assert 201 == response.status_code

    response_body = response.json()
    response_body.pop("id")
    assert expected_response == response_body


@pytest.mark.parametrize(
    "body",
    [
        ({"name": "s", "description": "Too short Name"}),
        ({"name": "This name is intentionally set too long"}),
        ({}),
        ({"description": "Forget to set name field"}),
        ({"name": "Too long description", "description": "".zfill(501)}),
    ]
)
def test_create_craftplan_success(body, db_mock):
    response = client.post(CREATE_PATH, json=body)

    assert 422 == response.status_code
