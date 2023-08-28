from abc import ABC

from car import Car
# CapuletEngine inherits from both Car and ABC (multiple inheritance)
# constructor takes in three parameters: last_service_date, current_mileage, last_service_mileage

class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

# method calculates whether the engine should be serviced based on mileage.
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000

# since inheritance needs a needs_service() method 
# def needs_service(self):
#         return self.engine_should_be_serviced()
    