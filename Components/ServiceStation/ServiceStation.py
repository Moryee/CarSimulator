from dataclasses import dataclass
from Components.Cars.Template import Car


@dataclass
class ServiceStation:
    _cars_served = 0

    @classmethod
    def repair(cls, car: Car):
        cls._cars_served += 1

    @classmethod
    def change_tires(cls, car: Car):
        cls._cars_served += 1

    @classmethod
    def wash(cls, car: Car):
        cls._cars_served += 1
