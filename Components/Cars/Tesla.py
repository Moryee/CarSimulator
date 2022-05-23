from dataclasses import dataclass
from .Template.Car import Car


@dataclass()
class Tesla(Car):
    _maximum_speed: int = 281

    def __repr__(self):
        return "Changed __repr__"
