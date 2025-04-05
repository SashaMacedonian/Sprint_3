from random import randint
import pytest


@pytest.fixture
def random_int():
    return str(randint(0, 1000))
