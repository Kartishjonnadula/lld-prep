from enum import Enum


class BookingStatus(Enum):

    PENDING_PAYMENT = "PENDING_PAYMENT"

    CONFIRMED = "CONFIRMED"

    FAILED = "FAILED"

    CANCELLED = "CANCELLED"
