class Animal:
    def talk(self):
        
        print(f"Animal can - talk")
class Dog(Animal):
    def bark(self):
        print(f"Animal-can bark")
d = Dog()
d.bark()
d.talk()


print("examples -2")


class Animal:
    def __init__(self,name,age):

        self.name = name
        self.age = age
    def talk(self):
        print(f"{self.name}- can talk and his age is : {self.age}")
class Dog(Animal):
    def __init__(self,name,age,food):
        super().__init__(name,age)
        self.food = food
    def bark(self):
        print(f"Pet Named {self.name} is {self.age} years old, will have only {self.food} as food.")

d = Dog("Bonkers",4,"Chicken")
d.bark()
d.talk()
        
        