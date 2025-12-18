from enum import Enum
from abc import ABC, abstractmethod

class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0


class ElevatorState(Enum):
    MOVING = 1
    IDLE = 2
class ElevatorSelectionStrategy(ABC):
    @abstractmethod
    def select_elevator(self, elevators: List, request: Request) -> Optional:
        pass

class NearestElevatorStrategy(ElevatorSelectionStrategy):
    def select_elevator(self, elevators: List, request: Request) -> Optional:
        best_elevator = None
        min_distance = float('inf')

        for elevator in elevators:
            if self._is_suitable(elevator, request):
                distance = abs(elevator.get_current_floor() - request.target_floor)
                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator

        return best_elevator

    def _is_suitable(self, elevator, request: Request) -> bool:
        if elevator.get_direction() == Direction.IDLE:
            return True
        if elevator.get_direction() == request.direction:
            if request.direction == Direction.UP and elevator.get_current_floor() <= request.target_floor:
                return True
            if request.direction == Direction.DOWN and elevator.get_current_floor() >= request.target_floor:
                return True
        return False

class Elevator:
    def __init__(self, elevator_id: int):
        self.id = elevator_id
        self.current_floor = 1
        self.current_floor_lock = threading.Lock()
        self.state = IdleState()
        self.is_running = True
        self.up_requests = set()
        self.down_requests = set()
        