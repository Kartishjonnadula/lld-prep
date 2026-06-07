from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from seats.seat_state import SeatState
from seats.seat import Seat


@dataclass
class ShowSeat:
    seat: Seat
    state: SeatState = SeatState.AVAILABLE

    locked_by_user_id: Optional[str] = None
    lock_expiry: Optional[datetime] = None

    def is_available(self) -> bool:

        if self.state == SeatState.AVAILABLE:
            return True

        if (
            self.state == SeatState.LOCKED
            and self.lock_expiry
            and datetime.now() > self.lock_expiry
        ):
            return True

        return False
