from __future__ import annotations

from typing import List, Optional

from game import Game


class Lane:
    """
    One physical lane that can run at most one active game at a time.
    """

    def __init__(self, lane_id: int) -> None:
        if lane_id <= 0:
            raise ValueError("lane_id must be a positive integer")

        self.lane_id = lane_id
        self._active_game: Optional[Game] = None

    def is_free(self) -> bool:
        return self._active_game is None or self._active_game.is_complete()

    def start_game(self, player_names: List[str]) -> Game:
        if not self.is_free():
            raise ValueError(f"Lane {self.lane_id} is busy with an active game")

        self._active_game = Game(player_names)
        return self._active_game

    def active_game(self) -> Game:
        if self._active_game is None:
            raise ValueError(f"Lane {self.lane_id} has no active game")
        return self._active_game

    def roll(self, pins_knocked: int) -> None:
        self.active_game().roll(pins_knocked)
