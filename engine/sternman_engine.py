from abc import ABC

from car import Car
# Sternman engine inherits from both Car and ABC
# constructor takes two parameters : last_service_date, warning_light_is_on
# last_service_date is attribute inherited from the Car class 

class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

# if the warning_light_is_on is true return true else return false
    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
