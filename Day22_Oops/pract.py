class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("This is examples")
    def test(self):
        print(self.name, ":", self.age)
Person("Ait",24).test()
# print(Person("A"))


class Demo:
    def __init__(self):
        self.name = "Deepik"
        self.age = 25
    def m1(self):
        print(self.name)
        print(self.age)
d = Demo()
d.m1()


class Student():
    def display(self):
        # self.name = "deepika"
        # self.age = 25
        print(self.name, ":", self.age)
    def disp(self):
        # self.role = "Trainer"
        print(self.role, self.name)
s = Student("Deepika",25,"Trainer")
s.display()
s.disp( )