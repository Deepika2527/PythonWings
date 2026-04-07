class Test:
    def __init__(self,name):
        self.name = name
    def test(self):
        print(self.name)
t = Test("Test1")
# t.test()
print(t.name)
print(t.__dict__)


class Demo:
    def __init__(self,name):
        self.name = name
    def m1(self,role):
        self.role = role
        print(f"My name is {self.name} and Role is {self.role}")
        # del self.role
        # print(f"My name is {self.name} and Role is {self.role}")
d = Demo("emp1")
d.m1("Developer")
print(d.__dict__)
print("Using object refrence")
d.company = "xyz"
print(d.__dict__)
d.role = "Tester"
print(d.__dict__)
d1 = Demo("emp2")
d1.m1("Designer")


        


