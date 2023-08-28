from abc import ABC, abstractmethod

# ABC abstract base class : used in python to define a blueprint for other classes (like an abstract class in java)
# class Car(ABC) : this defines a class called Car that inherits from the 'ABC' class 
# all classes that inherit from Car will need a needs_service() 
# def __init__(self, last_service_date): Is the constructor method it takes in an argument last_service_date and initalises a varibale with the same name 
# python the constructor method init is a special method that gets called when you create a new instance of the class
#  self parameter refers to the instance being created

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

# needs_service is an abstract method, classes that inherit this method must provide an implementation of the method
    @abstractmethod
    def needs_service(self):
        pass
# abstract method declaration doesnt have a body to the method so the subclass car will need to provide their own implemenation 