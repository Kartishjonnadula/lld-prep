from enum import Enum


class SeatState(Enum):
    AVAILABLE = "available"
    LOCKED = "locked"
    BOOKED = "booked"
