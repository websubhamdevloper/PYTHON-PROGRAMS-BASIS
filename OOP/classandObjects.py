
class Car:
    count = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.count += 1

    def get_brand(self):
        return self.__brand  + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"




mycar = Car("Toyota", "Corolla")
print(mycar.get_brand())
print(mycar.model)

_mycar = Car("Tata", "Safari")
print(f"{_mycar.get_brand()} , {_mycar.model}")

print(mycar.full_name(), _mycar.full_name())

tesla = ElectricCar("Tesla", "Model-S", "85kWh")
print(tesla.get_brand(), tesla.model, tesla.battery_size)

print(tesla.full_name())
print(tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

print(Car.count)

