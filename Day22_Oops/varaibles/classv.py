# class Test:
#     x  = 10
#     def __init__(self):
#         self.y = 20
#     def m1(self):
#         self.z = 30
#         print(self.z)


# t1 = Test()
# t2 = Test()
# t3 = Test()
# t1.m1()
# print(t1.__dict__)
# print(Test.__dict__)

# print("Pring the values of class and intance-before")
# print("T1 : ", t1.x,t1.y)
# print("T2 : ", t2.x,t2.y)
# print("T3 : ", t3.x,t3.y)

# Test.x = 100

# t2.y = 200

# print("Pring the values of class and intance-After")
# print("T1 : ", t1.x,t1.y)
# print("T2 : ", t2.x,t2.y)
# print("T3 : ", t3.x,t3.y)
# print("Creating class varaible outside the  object creation")
# Test.a = "A"
# print(Test.__dict__)



# class Demo:
#     def __init__(self):
#         self.x = "X"
#     def m1(self):
#         # creating class varaible using ClassName.varaibble_name = value
#         Demo.y = "Y"
#         print(Demo.y)
    
# d = Demo()
# d.m1()
# print("using className with __dict__")
# print(Demo.__dict__)
# print("Using object with dict")
# print(d.__dict__)



class Test:
    age = 24
    def __init__(self):
        self.x = 10  
    @classmethod
    def m1(cls):
        cls.y =100
        print(cls.y)
    @staticmethod
    def m2():
        Test.name = "Anu"
        print(Test.name)
t = Test()
t.m1()
print(Test.__dict__)
print(t.__dict__)
t.m2()
print(Test.__dict__)
print(t.__dict__)




