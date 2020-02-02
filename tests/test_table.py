import table
import pytest
import datetime


@pytest.fixture
def twelve_top():
    return table.Table(seats=12)


christmas = datetime.date(2029, 12, 25)
new_years_day = datetime.date(2030, 1, 1)


def test_init(twelve_top):
    assert twelve_top.seats == 12

