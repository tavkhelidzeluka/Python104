"""
class Car:
    count = 0  # static Attribute

    def __init__(self, brand: str) -> None:
        # initialize
        self.brand = brand
        Car.count += 1
    
    def __del__(self):
        Car.count -= 1

    @staticmethod
    def get_count() -> int:
        return Car.count


# Car.brand
my_car = Car("Mercedes")
print(Car.count)
my_car_2 = Car("Toyota")

print(my_car.brand)
del my_car_2
print(my_car_2.brand)
print(Car.count)

"""

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.driver = 'Marco'
        self.__n = "I'm Private Attribute" # Private Attribute
        self._l = "I'm Protected Attribute" # Protected Attribute
    
    def _protected_method(self):
        print(self.__n, 'Called From protected Method')
    
    @abstractmethod
    def move(self):
        pass

    def __str__(self) -> str:
        return f'{self.brand} - {self.driver}'


class Car(Transport):
    def __init__(self, brand: str, wheels: int = 4) -> None:
        super().__init__(brand)
        self.__wheels = self.set_wheels(wheels)  # private attribute
        # Transport.__init__(self, brand)
    
    def set_wheels(self, wheels: int) -> None:
        if wheels < 0:
            raise ValueError("Wheel Count must be higher than 0")
        self.__wheels = wheels
    
    def get_wheels(self) -> int:
        return self.__wheels
    
    def move(self):
        print("Drive")

    def __str__(self) -> str:
        return f'{super().__str__()} - {self.__wheels} - {self._l}'


class Boat(Transport):
    def move(self):
        print("Float")


class Airplane(Transport):
    def move(self):
        print("Flies")

    def go_up():
        pass

    def go_down():
        pass


class Dog:
    def __init__(self) -> None:
        pass


my_transport: list[Transport] = [
    Car("Mercedes"),
    Boat("Mercedes"),
    Airplane("Mercedes")
]

"""
my_car = Car("Mercedes")
boat = Boat("Mercedes")
plane = Airplane("Mercedes")

print(my_car.brand)
# my_car.move()
# boat.move()
# plane.move()
"""

# my_transport[0].__wheels = -1

my_transport[0].set_wheels(1)
print(my_transport[0].get_wheels())
for transport in my_transport:
    print('-' * 10)

    print(transport)
    transport.move()
    transport._protected_method()
    print('-' * 10)
