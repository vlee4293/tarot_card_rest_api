import json

import pytest
from fastapi.testclient import TestClient

from tarot_cards_rest.main import api


client = TestClient(api)


@pytest.fixture
def not_found_id():
    yield -1


@pytest.fixture
def invalid_id():
    yield "@"


def test_get_tarot_fool():
    with open("tests/responses/get_tarot_fool.json", "r") as fp:
        response = client.get("/tarots/1")
        assert response.status_code == 200
        assert response.json() == json.load(fp)


def test_get_tarot_404(not_found_id):
    response = client.get(f"/tarots/{not_found_id}")
    assert response.status_code == 404


def test_get_tarot_422(invalid_id):
    response = client.get(f"/tarots/{invalid_id}")
    assert response.status_code == 422


def test_get_tarot_fool_fortunes():
    with open("tests/responses/get_tarot_fool_fortunes.json", "r") as fp:
        response = client.get("/tarots/1/fortunes")
        assert response.status_code == 200
        assert response.json() == json.load(fp)


def test_get_tarot_fool_keywords():
    with open("tests/responses/get_tarot_fool_keywords.json", "r") as fp:
        response = client.get("/tarots/1/keywords")
        assert response.status_code == 200
        assert response.json() == json.load(fp)


def test_get_tarot_fool_meanings():
    with open("tests/responses/get_tarot_fool_meanings.json", "r") as fp:
        response = client.get("/tarots/1/meanings")
        assert response.status_code == 200
        assert response.json() == json.load(fp)


def test_get_arcana_major():
    with open("tests/responses/get_arcana_major.json", "r") as fp:
        response = client.get("/arcanas/1")
        assert response.status_code == 200
        assert response.json() == json.load(fp)


def test_get_suit_trump():
    with open("tests/responses/get_suit_trump.json", "r") as fp:
        response = client.get("/suits/1")
        assert response.status_code == 200
        assert response.json() == json.load(fp)
