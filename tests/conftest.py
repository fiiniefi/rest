from pytest import fixture
from starlette.testclient import TestClient

from src.conf.builder import APIBuilder


@fixture
def app():
    return APIBuilder().build()


@fixture
def api_client(app):
    return TestClient(app)
