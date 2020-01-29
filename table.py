
class Table:
    def __init__(self, seats):
        self.seats = seats
        self.available = seats

    def request_reservation_for(self, reservation_date, requested_count):
        if requested_count <= self.available:
            self.available -= requested_count
            return True
        else:
            return False