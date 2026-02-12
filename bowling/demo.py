import random
from typing import Optional

from bowling_alley_system import BowlingAlleySystem
from frames import FinalFrame, NormalFrame
from roll import Roll


def play_one_turn(system: BowlingAlleySystem, lane_id: int, planned_rolls: dict[str, list[int]]) -> None:
    game = system.lane(lane_id).active_game()
    current_player = game.current_player().name

    if not planned_rolls[current_player]:
        raise ValueError(f"No planned rolls left for player: {current_player}")

    pins_knocked = planned_rolls[current_player].pop(0)
    system.roll(lane_id, pins_knocked)


def random_roll_for_current_player(system: BowlingAlleySystem, lane_id: int, rng: random.Random) -> int:
    game = system.lane(lane_id).active_game()
    frame = game.current_player().current_frame()
    rolls = frame.rolls

    if isinstance(frame, NormalFrame):
        if not rolls:
            return rng.randint(0, Roll.MAX_PINS)
        return rng.randint(0, Roll.MAX_PINS - rolls[0].pins_knocked)

    if isinstance(frame, FinalFrame):
        if not rolls:
            return rng.randint(0, Roll.MAX_PINS)

        if len(rolls) == 1:
            first = rolls[0].pins_knocked
            if first == Roll.MAX_PINS:
                return rng.randint(0, Roll.MAX_PINS)
            return rng.randint(0, Roll.MAX_PINS - first)

        if len(rolls) == 2:
            first = rolls[0].pins_knocked
            second = rolls[1].pins_knocked
            if first == Roll.MAX_PINS and second < Roll.MAX_PINS:
                return rng.randint(0, Roll.MAX_PINS - second)
            return rng.randint(0, Roll.MAX_PINS)

    raise RuntimeError("Unsupported frame type or invalid frame state for random roll generation")


def main(use_random_rolls: bool = False, seed: Optional[int] = None) -> None:
    system = BowlingAlleySystem(lane_count=2)
    rng = random.Random(seed)

    lane_1 = system.start_game_on_any_free_lane(["Alice", "Bob"])
    lane_2 = system.start_game_on_any_free_lane(["Carol"])

    planned_rolls_by_lane: dict[int, dict[str, list[int]]] = {
        lane_1: {
            "Alice": [10] * 12,  # Perfect game.
            "Bob": [9, 0] * 10,  # 90 points.
        },
        lane_2: {
            "Carol": [5, 4] * 10,  # 90 points.
        },
    }

    while True:
        progressed = False
        for lane_id, planned_rolls in planned_rolls_by_lane.items():
            game = system.lane(lane_id).active_game()
            if game.is_complete():
                continue

            if use_random_rolls:
                system.roll(lane_id, random_roll_for_current_player(system, lane_id, rng))
            else:
                play_one_turn(system, lane_id, planned_rolls)
            progressed = True

        if not progressed:
            break

    for lane_id in sorted(planned_rolls_by_lane.keys()):
        game = system.lane(lane_id).active_game()
        print(f"Lane {lane_id}")
        print(f"Scores: {game.scores()}")
        print(f"Running Scores: {game.running_scores()}")
        print(f"Winner: {game.winner().name}")
        print("-" * 40)

    print(f"Free lanes after completion: {system.free_lane_ids()}")


if __name__ == "__main__":
    main()
