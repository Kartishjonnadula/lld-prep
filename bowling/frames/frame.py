from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from roll import Roll


class Frame(ABC):
    """
    Base abstraction for one bowling frame.
    """

    def __init__(self) -> None:
        self._rolls: List[Roll] = []

    @property
    def rolls(self) -> List[Roll]:
        return list(self._rolls)

    @abstractmethod
    def add_roll(self, roll: Roll) -> None:
        pass

    @abstractmethod
    def is_complete(self) -> bool:
        pass

    def is_strike(self) -> bool:
        # strike is when all 10 pins are knocked down in the first roll of the frame
        return len(self._rolls) >= 1 and self._rolls[0].pins_knocked == Roll.MAX_PINS

    def is_spare(self) -> bool:
        #spare is when all 10 pins are knocked down in the first two rolls of the frame, but not a strike
        if len(self._rolls) < 2 or self.is_strike():
            return False
        return self._rolls[0].pins_knocked + self._rolls[1].pins_knocked == Roll.MAX_PINS

    def pins_knocked(self) -> int:
        return sum(r.pins_knocked for r in self._rolls)
