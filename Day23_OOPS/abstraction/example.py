
from abc import ABC,abstractmethod





print("This is abrtact class examples")
class Amount(ABC):
    @abstractmethod
    def gpay(self):
        pass
    @abstractmethod
    def phonepe(self):
        pass
    def checking(self):
        print("Dont worry it is safe")



class CheckBal(Amount):
    def gpay(self):
        print(f"Using gpay i payed the amount")
    def phonepe(self):
        print(f"Using phonepe i payed the amount")
c = CheckBal()
c.gpay()
c.phonepe()
c.checking()
        






print("Interface clas")
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("The car has started....")
#     def stop(self):
#         print("The car is stopped...")
# c = Car()
# c.start()
# c.stop()










# class Test:
#     def __init__(self):
#         pass
#     def m1(self):
#         pass
# print("Concrete class")
# class Studnet():
#     def __init__(self,name):
#         self.name = name
#     def m1(self,age):
#         self.age = age
#         print(f"{self.name}- {self.age}")
# s = Studnet("Anu")
# s.m1(22)

