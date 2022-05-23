from dataclasses import dataclass
from Components.Cars.Template import Car


@dataclass
class ServiceStation:
    _cars_served = 0

    @property
    def cars_served(self):
        return ServiceStation._cars_served

    @cars_served.setter
    def cars_served(self, value):
        ServiceStation._cars_served = value

    @classmethod
    def repair(cls, car: Car):
        ServiceStation.cars_served += 1

    @classmethod
    def change_tires(cls, car: Car):
        ServiceStation.cars_served += 1

    @classmethod
    def wash(cls, car: Car):
        ServiceStation.cars_served += 1
