from dataclasses import dataclass
from .Template.Car import Car


@dataclass
class Audi(Car):
    _maximum_speed: int = 332
