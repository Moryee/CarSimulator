from abc import ABC, abstractmethod


class CarAbstract(ABC):
    @property
    @abstractmethod
    def maximum_speed(self):
        pass

    @abstractmethod
    def gas(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def engine_on_off(self):
        pass

    @abstractmethod
    def hand_brake_on_off(self):
        pass

    @abstractmethod
    def print_status(self):
        pass
