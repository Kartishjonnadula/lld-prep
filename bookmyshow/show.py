from screen import Screen
from datetime import datetime, timedelta
from seats.show_seat import ShowSeat
from seats.seat_state import SeatState
from threading import RLock
from booking.booking import Booking
from booking.booking_status import BookingStatus

from threading import RLock


class Show:

    def __init__(
        self, show_id: str, movie: Movie, screen: Screen, category_prices: dict
    ):

        self.show_id = show_id

        self.movie = movie

        self.screen = screen

        self.category_prices = category_prices

        self.lock = RLock()

        self.show_seats = {seat.seat_id: ShowSeat(seat) for seat in screen.seats}

    def lock_seats(self, user_id: str, seat_ids: list[str]) -> bool:
        with self.lock:
            requested_seats = [self.show_seats[seat_id] for seat_id in seat_ids]

            for seat in requested_seats:

                if not seat.is_available():
                    return False

            expiry = datetime.now() + timedelta(minutes=5)

            for seat in requested_seats:

                seat.state = SeatState.LOCKED
                seat.locked_by_user_id = user_id
                seat.lock_expiry = expiry

        return True

    def confirm_booking(self, booking: Booking) -> bool:

        with self.lock:

            for seat_id in booking.seat_ids:

                show_seat = self.show_seats[seat_id]

                if show_seat.state != SeatState.LOCKED:
                    return False

            for seat_id in booking.seat_ids:

                show_seat = self.show_seats[seat_id]

                show_seat.state = SeatState.BOOKED
                show_seat.locked_by_user_id = None
                show_seat.lock_expiry = None

            booking.status = BookingStatus.CONFIRMED

            return True

    def release_booking(self, booking: Booking):

        with self.lock:
            for seat_id in booking.seat_ids:

                seat = self.show_seats[seat_id]

                seat.state = SeatState.AVAILABLE
                seat.locked_by_user_id = None
                seat.lock_expiry = None

            booking.status = BookingStatus.FAILED

    def get_price(self, seat_id: str) -> float:

        seat = self.show_seats[seat_id].seat

        return self.category_prices[seat.seat_category]
