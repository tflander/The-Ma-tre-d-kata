import table
import pytest

@pytest.fixture
def twelve_top():
    return table.Table(seats=12)


def test_init(twelve_top):
    assert twelve_top.seats == 12
    assert twelve_top.available == 12


def test_takes_reservation_for_empty_table(twelve_top):
    assert twelve_top.request_reservation_for(10)
    assert twelve_top.seats == 12
    assert twelve_top.available == 2


def test_does_not_take_reservation_for_full_table(twelve_top):
    twelve_top.request_reservation_for(12)
    assert twelve_top.seats == 12
    assert twelve_top.available == 0
    assert twelve_top.request_reservation_for(1) == False


def test_does_not_take_reservation_for_more_than_the_table_holds(twelve_top):
    assert twelve_top.request_reservation_for(13) == False
    assert twelve_top.seats == 12
    assert twelve_top.available == 12
