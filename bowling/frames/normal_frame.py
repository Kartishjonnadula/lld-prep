from roll import Roll

from .frame import Frame


class NormalFrame(Frame):
    """
    Frames 1-9.
    """

    def add_roll(self, roll: Roll) -> None:
        if self.is_complete():
            raise ValueError("Cannot add roll: normal frame is already complete")

        if len(self._rolls) == 1:
            first = self._rolls[0].pins_knocked
            if first + roll.pins_knocked > Roll.MAX_PINS:
                raise ValueError("Total pins in a normal frame cannot exceed 10")

        self._rolls.append(roll)

    #its complete when roll is strike or when we have two rolls in the frame
    def is_complete(self) -> bool:
        if not self._rolls:
            return False
        if self._rolls[0].pins_knocked == Roll.MAX_PINS:
            return True
        return len(self._rolls) == 2
