import table
from restaurant import *

def test_one_table_botique_restaurant():
    twelve_top = table.Table(seats=12)
    botique_restaurant = Restaurant(RestaurantType.BOUTIQUE, twelve_top)