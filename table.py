
class Table:

    def __init__(self, seats):
        self.seats = seats
        # self.available = seats
        self.reservations = dict()

    def request_reservation_for(self, reservation_date, requested_count):

        current_seats_reserved_count = 0;
        if reservation_date in self.reservations:
            current_seats_reserved_count = self.reservations[reservation_date]

        if requested_count + current_seats_reserved_count <= self.seats:
            self.reservations[reservation_date] = requested_count + current_seats_reserved_count
            return True
        else:
            return False

    def available_for(self, reservation_date):
        if reservation_date in self.reservations:
            return self.seats - self.reservations[reservation_date]
        else:
            return self.seats
