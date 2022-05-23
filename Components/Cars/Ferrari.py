from dataclasses import dataclass
from .Template.Car import Car


@dataclass
class Ferrari(Car):
    _maximum_speed: int = 317
