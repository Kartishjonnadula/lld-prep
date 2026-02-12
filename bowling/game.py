from __future__ import annotations

from typing import List

from player import Player


class Game:
    """
    One bowling game on a single lane for multiple players.
    """

    MIN_PLAYERS = 1

    def __init__(self, player_names: List[str]) -> None:
        if len(player_names) < self.MIN_PLAYERS:
            raise ValueError("At least one player is required to start a game")

        self._players: List[Player] = [Player(name) for name in player_names]
        self._current_player_index = 0

    @property
    def players(self) -> List[Player]:
        return list(self._players)

    def current_player(self) -> Player:
        return self._players[self._current_player_index]

    def roll(self, pins_knocked: int) -> None:
        if self.is_complete():
            raise ValueError("Cannot roll: game is already complete")

        player = self.current_player()
        frame_before = player.current_frame()
        if frame_before.is_complete():
            raise RuntimeError("Current frame cannot be complete before roll")

        player.roll(pins_knocked)

        frame_after = player.current_frame()
        moved_to_next_frame = frame_after is not frame_before
        if moved_to_next_frame or player.is_game_complete():
            self._advance_turn()

    def is_complete(self) -> bool:
        return all(player.is_game_complete() for player in self._players)

    def scores(self) -> dict[str, int]:
        return {player.name: player.total_score() for player in self._players}

    def running_scores(self) -> dict[str, List[int]]:
        return {player.name: player.frame_scores() for player in self._players}

    def winner(self) -> Player:
        if not self.is_complete():
            raise ValueError("Winner is available only after game completion")
        return max(self._players, key=lambda p: p.total_score())

    def _advance_turn(self) -> None:
        if self.is_complete():
            return

        player_count = len(self._players)
        for step in range(1, player_count + 1):
            next_index = (self._current_player_index + step) % player_count
            if not self._players[next_index].is_game_complete():
                self._current_player_index = next_index
                return
