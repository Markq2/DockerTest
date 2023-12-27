import pytest


@pytest.fixture
def hello():
    print('In Fixture')
