from dataclasses import dataclass

from .CarAbstract import CarAbstract


class AccelerationError(Exception):
    pass


class HandBrakeError(Exception):
    pass


@dataclass(repr=False)
class Car(CarAbstract):
    _engine: bool = False
    _hand_brake: bool = True
    _speed: int = 0
    _maximum_speed: int = 100

    # Properties
    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value: bool):
        self._engine = value

    @property
    def hand_brake(self):
        return self._hand_brake

    @hand_brake.setter
    def hand_brake(self, value: bool):
        self._hand_brake = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value > self._maximum_speed:
            self._speed = self.maximum_speed
        elif value < 0:
            self._speed = 0
        else:
            self._speed = value

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @maximum_speed.setter
    def maximum_speed(self, value):
        self._maximum_speed = value

    # Methods
    def gas(self):
        if not self.engine:
            raise AccelerationError("Turn on the engine")

        if self.hand_brake:
            raise AccelerationError("Release the handbrake")

        self.speed += 10

    def brake(self):
        self.speed -= 10

    def engine_on_off(self):
        if self.engine:
            self.engine = False
        else:
            self.engine = True

    def hand_brake_on_off(self):
        if self.hand_brake:
            self.hand_brake = False
        elif self.speed == 0:
            self.hand_brake = True
            return
        elif self.speed > 0:
            raise HandBrakeError("Slow down")

    def print_status(self):
        print()
        print(f"Speed: {self.speed}")
        print(f"Engine: {self.engine}")
        print(f"Hand brake: {self.hand_brake}")

    # magic methods
    def __str__(self):
        return f"{self.__class__.__name__}(\
            Engine: {self.engine}, \
            HandBrake: {self.hand_brake}, \
            Speed: {self.speed}, \
            MaximumSpeed: {self.maximum_speed}\
        )"

    def __gt__(self, other: CarAbstract):
        return self.maximum_speed > other.maximum_speed

    def __lt__(self, other):
        return self.maximum_speed < other.maximum_speed

    def __copy__(self):
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        return newone
