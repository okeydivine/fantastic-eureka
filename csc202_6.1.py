class Car:
    def __init__(self, make, year_model):
        self.__make = make
        self.__year_model = year_model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -=5

    def get_speed(self):
        return self.__speed

def main():
    my_car = Car("Toyota", "Camry 2008")
    for i in range(5):
        my_car.accelerate()
        print("My Car's speed: ", my_car.get_speed())
    for i in range(5):
        my_car.brake()
        print("Car's speed after pulling brakes: ", my_car.get_speed())
main ()
