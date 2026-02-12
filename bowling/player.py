from __future__ import annotations

from typing import List

from frames import FinalFrame, Frame, NormalFrame
from roll import Roll


class Player:
    TOTAL_FRAMES = 10

    def __init__(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Player name must be a non-empty string")

        self.name = name.strip()
        self._frames: List[Frame] = [NormalFrame() for _ in range(self.TOTAL_FRAMES - 1)]
        self._frames.append(FinalFrame())

    @property
    def frames(self) -> List[Frame]:
        return list(self._frames)

    def roll(self, pins_knocked: int) -> None:
        if self.is_game_complete():
            raise ValueError(f"Cannot roll: game is already complete for player {self.name}")

        roll = Roll(pins_knocked)
        self.current_frame().add_roll(roll)

    def current_frame(self) -> Frame:
        for frame in self._frames:
            if not frame.is_complete():
                return frame
        return self._frames[-1]

    def is_game_complete(self) -> bool:
        return all(frame.is_complete() for frame in self._frames)

    def total_score(self) -> int:
        total = 0

        for frame_index in range(self.TOTAL_FRAMES):
            frame = self._frames[frame_index]
            if not frame.rolls:
                break

            total += self._frame_score(frame_index)

        return total

    def frame_scores(self) -> List[int]:
        """
        Returns running total score after each frame.
        """
        running_scores: List[int] = []
        running_total = 0

        for frame_index in range(self.TOTAL_FRAMES):
            frame = self._frames[frame_index]
            if not frame.rolls:
                break

            running_total += self._frame_score(frame_index)
            running_scores.append(running_total)

        return running_scores

    def _frame_score(self, frame_index: int) -> int:
        frame = self._frames[frame_index]

        if frame_index == self.TOTAL_FRAMES - 1:
            return frame.pins_knocked()

        if frame.is_strike():
            return frame.pins_knocked() + sum(self._next_rolls_after_frame(frame_index, 2))
        if frame.is_spare():
            return frame.pins_knocked() + sum(self._next_rolls_after_frame(frame_index, 1))
        return frame.pins_knocked()

    def _next_rolls_after_frame(self, frame_index: int, count: int) -> List[int]:
        next_rolls: List[int] = []

        for next_frame in self._frames[frame_index + 1 :]:
            for roll in next_frame.rolls:
                next_rolls.append(roll.pins_knocked)
                if len(next_rolls) == count:
                    return next_rolls

        return next_rolls
