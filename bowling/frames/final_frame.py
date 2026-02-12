from roll import Roll

from .frame import Frame


class FinalFrame(Frame):
    """
    Frame 10.
    """

    def add_roll(self, roll: Roll) -> None:
        if self.is_complete():
            raise ValueError("Cannot add roll: final frame is already complete")

        if len(self._rolls) == 1:
            first = self._rolls[0].pins_knocked
            if first != Roll.MAX_PINS and first + roll.pins_knocked > Roll.MAX_PINS:
                raise ValueError(
                    "In final frame, first two rolls cannot exceed 10 unless first is a strike"
                )

        if len(self._rolls) == 2:
            first = self._rolls[0].pins_knocked
            second = self._rolls[1].pins_knocked
            bonus_roll_allowed = first == Roll.MAX_PINS or first + second == Roll.MAX_PINS
            if not bonus_roll_allowed:
                raise ValueError("Third roll allowed only after a strike or spare in final frame")

            # If first was strike and second was not, third roll uses remaining pins.
            if first == Roll.MAX_PINS and second < Roll.MAX_PINS:
                if second + roll.pins_knocked > Roll.MAX_PINS:
                    raise ValueError(
                        "After strike then non-strike in final frame, second and third rolls cannot exceed 10"
                    )

        self._rolls.append(roll)
    #its compelete when we have three rolls or when we have two rolls and they are not strike or spare
    def is_complete(self) -> bool:
        if len(self._rolls) < 2:
            return False
        if len(self._rolls) == 2:
            first = self._rolls[0].pins_knocked
            second = self._rolls[1].pins_knocked
            return not (first == Roll.MAX_PINS or first + second == Roll.MAX_PINS)
        return len(self._rolls) == 3
