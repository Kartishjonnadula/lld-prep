class Roll:
    """
    Value object for one bowling roll.

    Responsibility:
    - Hold how many pins were knocked down in a single attempt.
    - Enforce single-roll invariants only.
    """

    MAX_PINS = 10

    def __init__(self, pins_knocked: int) -> None:
        if not isinstance(pins_knocked, int):
            raise TypeError("pins_knocked must be an integer")
        if not 0 <= pins_knocked <= self.MAX_PINS:
            raise ValueError(
                f"pins_knocked must be between 0 and {self.MAX_PINS}, got {pins_knocked}"
            )
        self.pins_knocked = pins_knocked
