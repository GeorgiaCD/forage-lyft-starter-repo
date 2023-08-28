from abc import ABC

from car import Car

# inherits from Car and ABC
# constructor takes in three parameters: last_service_date, current_mileage, last_service_mileage

class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

# method engine_should_be_serviced if the difference between the two mileages is greater than 60000
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
