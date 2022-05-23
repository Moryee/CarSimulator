import keyboard
import time

from Components.Cars.Audi import Audi
from Components.Cars.Ferrari import Ferrari
from Components.Cars.Tesla import Tesla
from Components.Cars.Template.Car import Car
from Components.ServiceStation.ServiceStation import ServiceStation


def drive(car: Car) -> None:
    while True:
        button = keyboard.read_key()
        time.sleep(0.3)
        if button == 'w':
            car.gas()
            car.print_status()
        elif button == 's':
            car.brake()
            car.print_status()
        elif button == 'e':
            car.engine_on_off()
            car.print_status()
        elif button == 'space':
            car.hand_brake_on_off()
            car.print_status()
            time.sleep(0.1)
        elif button == 'esc':
            print("break")
            break


def menu(car: Car) -> None:
    print()
    while True:
        print("drive/repair/wash/tires/exit")
        choice = input()
        if choice == "drive":
            drive(car)
        elif choice == "repair":
            ServiceStation.repair(car)
        elif choice == "wash":
            ServiceStation.wash(car)
        elif choice == "tires":
            ServiceStation.wash(car)
        elif choice == "exit":
            break



if __name__ == "__main__":
    tesla = Tesla()  # not necessary

    
    # menu(tesla)
    tesla.print_status()
