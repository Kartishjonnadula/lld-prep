from enum import Enum
import uuid
from abc import ABC,abstractmethod
from datetime import datetime
import math
class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    TRUCK = 3

'''
    entities
    vehicle
    ParkingFloor
    ParkingSpot
    ParkingLot
    Ticket
    PricingStrategy
'''



class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
class ParkingSpot:
        def __init__(self, spot_id: str, allowed_types: list[VehicleType]):
            self.spot_id = spot_id
            self.allowed_types = allowed_types
            self.occupied_by: Vehicle | None = None
        def can_fit(self, vehicle: Vehicle) -> bool:
            return vehicle.vehicle_type in self.allowed_types and self.occupied_by is None

        def park(self, vehicle: Vehicle):
            self.occupied_by = vehicle
        def leave(self):
            self.occupied_by = None        
class ParkingFloor:
    def __init__(self, floor_number: int, spots: list[ParkingSpot]):
        self.floor_number = floor_number
        self.spots = spots

    def find_spot(self, vehicle: Vehicle) -> ParkingSpot | None:
        for spot in self.spots:
            if spot.can_fit(vehicle):
                return spot
        return None

    def available_count(self, vehicle_type: VehicleType) -> int:
        return sum(1 for spot in self.spots
                   if vehicle_type in spot.allowed_types and spot.occupied_by is None)

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, ticket) -> float:
        pass
class FlatRatePricing(PricingStrategy):
    def __init__(self, rate: float):
        self.rate = rate

    def calculate_price(self, ticket) -> float:
        return self.rate

class HourlyPricing(PricingStrategy):
    def __init__(self, hourly_rate: float):
        self.hourly_rate = hourly_rate

    def calculate_price(self, ticket) -> float:
        duration = ticket.exit_time - ticket.entry_time
        hours = math.ceil(duration.total_seconds() / 3600)
        return hours * self.hourly_rate


class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time: datetime | None = None
        self.pricing_strategy=HourlyPricing()
        self.price = 0.0

class ParkingLot:
    _instance = None
    def __new__(cls, floors: list[ParkingFloor],pricing_strategy: PricingStrategy):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(floors,pricing_strategy)
        return cls._instance   
    def _init(self, floors,pricing_strategy):
        self.floors = floors
        self.active_tickets: dict[str, Ticket] = {}
        self.pricing_strategy = pricing_strategy
    def park_vehicle(self, vehicle: Vehicle) -> Ticket | None:
        # find first available spot
        for floor in self.floors:
            spot = floor.find_spot(vehicle)
            if spot:
                spot.park(vehicle)
                ticket = Ticket(vehicle, spot)
                self.active_tickets[ticket.ticket_id] = ticket
                return ticket
        return None  # no spot available
    def leave_vehicle(self, ticket_id: str) -> bool:
        ticket = self.active_tickets.get(ticket_id)
        if not ticket:
            return False

        ticket.spot.leave()
        ticket.exit_time = datetime.now()
        ticket.price = self.pricing_strategy.calculate_price(ticket)
        del self.active_tickets[ticket_id]
        return True
    def get_availability(self):
        return {
            floor.floor_number: {
                v: floor.available_count(v)
                for v in VehicleType
            }
            for floor in self.floors
        }

#price
