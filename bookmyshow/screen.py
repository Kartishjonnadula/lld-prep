from seats.seat import Seat


class Screen:

    def __init__(self, screen_id: str, seats: list[Seat]):
        self.screen_id = screen_id
        self.seats = seats
