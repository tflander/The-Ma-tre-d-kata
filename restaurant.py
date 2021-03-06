from enum import Enum
import reservation

class RestaurantType(Enum):
    BOUTIQUE = "boutique (shared seating)"
    # HAUSTE_CUISINE = "single seating"
    # SECOND_SEATING = "2 1/2 hours per seating"

class Restaurant:

    def __init__(self, restaurant_type, table):
        self.reservations = dict()
        self.table = table

    def request_reservation_for(self, reservation_date, requested_count):

        current_seats_reserved_count = 0;
        if reservation_date in self.reservations:
            current_seats_reserved_count = self.reservations[reservation_date].number_of_reserved_seats

        if requested_count + current_seats_reserved_count <= self.table.seats:
            self.reservations[reservation_date] = reservation.Reservation(reservation_date, self.table, requested_count + current_seats_reserved_count)
            return True
        else:
            return False

    def available_for(self, reservation_date):
        if reservation_date in self.reservations:
            return self.table.seats - self.reservations[reservation_date].number_of_reserved_seats
        else:
            return self.table.seats
