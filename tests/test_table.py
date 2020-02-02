import table
import pytest


@pytest.fixture
def twelve_top():
    return table.Table(seats=12)


def test_init(twelve_top):
    assert twelve_top.seats == 12

