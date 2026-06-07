import uuid

from booking.booking import Booking
from booking.booking_status import BookingStatus
from payment.payment_status import PaymentStatus


class BookingService:

    def __init__(self, payment_service):
        self.payment_service = payment_service

    def create_booking(self, user_id: str, show, seat_ids: list[str]):
        locked = show.lock_seats(user_id=user_id, seat_ids=seat_ids)
        if not locked:
            raise Exception("Requested seats are unavailable")

        booking = Booking(
            booking_id=str(uuid.uuid4()),
            user_id=user_id,
            show_id=show.show_id,
            seat_ids=seat_ids,
            status=BookingStatus.PENDING_PAYMENT,
        )
        try:
            total_amount = self._calculate_total_amount(show, seat_ids)
            payment = self.payment_service.process_payment(
                booking.booking_id, total_amount
            )
            if payment.status == PaymentStatus.SUCCESS:
                show.confirm_booking(booking)
            else:
                show.release_booking(booking)
        except Exception:
            show.release_booking(booking)
            raise

        return booking

    def _calculate_total_amount(self, show, seat_ids: list[str]) -> float:

        total = 0

        for seat_id in seat_ids:

            total += show.get_price(seat_id)

        return total
