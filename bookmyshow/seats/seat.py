from seats.seat_category import SeatCategory
from dataclasses import dataclass


@dataclass(frozen=True)
class Seat:
    seat_id: str
    seat_category: SeatCategory
