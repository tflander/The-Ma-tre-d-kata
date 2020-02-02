from enum import Enum

class RestaurantType(Enum):
    BOUTIQUE = "boutique (shared seating)"
    HAUsTE_CUISINE = "single seating"
    SECOND_SEATING = "2 1/2 hours per seating"

class Restaurant:

    def __init__(self, restaurant_type, table):
        pass