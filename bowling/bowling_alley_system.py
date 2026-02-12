from __future__ import annotations

from typing import Dict, List

from lane import Lane


class BowlingAlleySystem:
    """
    Coordinates multiple lanes so games can run in parallel.
    """

    def __init__(self, lane_count: int) -> None:
        if lane_count <= 0:
            raise ValueError("lane_count must be a positive integer")

        self._lanes: Dict[int, Lane] = {
            lane_id: Lane(lane_id) for lane_id in range(1, lane_count + 1)
        }

    def lane(self, lane_id: int) -> Lane:
        lane = self._lanes.get(lane_id)
        if lane is None:
            raise ValueError(f"Lane {lane_id} does not exist")
        return lane

    def free_lane_ids(self) -> List[int]:
        return [lane_id for lane_id, lane in self._lanes.items() if lane.is_free()]

    def start_game_on_lane(self, lane_id: int, player_names: List[str]) -> None:
        self.lane(lane_id).start_game(player_names)

    def start_game_on_any_free_lane(self, player_names: List[str]) -> int:
        free_lane_ids = self.free_lane_ids()
        if not free_lane_ids:
            raise ValueError("No free lanes available")

        lane_id = free_lane_ids[0]
        self.start_game_on_lane(lane_id, player_names)
        return lane_id

    def roll(self, lane_id: int, pins_knocked: int) -> None:
        self.lane(lane_id).roll(pins_knocked)
