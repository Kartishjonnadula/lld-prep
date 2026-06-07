from dataclasses import dataclass
from typing import List
from booking.booking_status import BookingStatus


@dataclass
class Booking:

    booking_id: str

    user_id: str

    show_id: str

    seat_ids: List[str]

    status: BookingStatus
