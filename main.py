import keyboard
import time

from Components.Cars.Audi import Audi
from Components.Cars.Ferrari import Ferrari
from Components.Cars.Tesla import Tesla
from Components.Cars.Template.Car import Car
from Components.ServiceStation.ServiceStation import ServiceStation


def drive(car: Car) -> None:
    car.print_status()
    while True:
        try:
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
        except Exception as e:
            print(f"!!! {e}")
            continue


def menu(car: Car) -> None:
    print()

    while True:
        print()
        print("drive/repair/wash/tires/exit")
        choice = input()
        if choice == "drive":
            drive(car)
        elif choice == "repair":
            ServiceStation.repair(car)
            print("Repaired")
        elif choice == "wash":
            ServiceStation.wash(car)
            print("Washed")
        elif choice == "tires":
            ServiceStation.change_tires(car)
            print("Tires Changed")
        elif choice == "exit":
            break
        else:
            print("!!! this menu does not exist")


if __name__ == "__main__":
    tesla = Tesla()
    menu(tesla)
