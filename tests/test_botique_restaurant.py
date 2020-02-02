import table
from restaurant import *

import pytest
import datetime


christmas = datetime.date(2029, 12, 25)
new_years_day = datetime.date(2030, 1, 1)


@pytest.fixture
def botique_restaurant():
    twelve_top = table.Table(seats=12)
    return Restaurant(RestaurantType.BOUTIQUE, twelve_top)


def test_init(botique_restaurant):
    twelve_top = botique_restaurant.table
    assert twelve_top.seats == 12
    assert botique_restaurant.available_for(new_years_day) == 12


def test_takes_reservation_for_empty_table(botique_restaurant):
    assert botique_restaurant.request_reservation_for(new_years_day, requested_count=10)
    assert botique_restaurant.available_for(new_years_day) == 2


def test_does_not_take_reservation_for_full_table(botique_restaurant):
    botique_restaurant.request_reservation_for(new_years_day, requested_count=12)
    assert botique_restaurant.available_for(new_years_day) == 0
    assert botique_restaurant.request_reservation_for(new_years_day, requested_count=1) == False


def test_does_not_take_reservation_for_more_than_the_table_holds(botique_restaurant):
    assert botique_restaurant.request_reservation_for(new_years_day, requested_count=13) == False
    assert botique_restaurant.available_for(new_years_day) == 12


def test_seats_different_parties_together(botique_restaurant):
    assert botique_restaurant.request_reservation_for(new_years_day, requested_count=3)
    assert botique_restaurant.request_reservation_for(new_years_day, requested_count=4)
    assert botique_restaurant.available_for(new_years_day) == 5


def tests_takes_reservation_for_different_days(botique_restaurant):
    assert botique_restaurant.request_reservation_for(christmas, requested_count=10)
    assert botique_restaurant.request_reservation_for(new_years_day, requested_count=10)
