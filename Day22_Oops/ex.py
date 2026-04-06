# class Demo:
#     '''This is Demo'''
# d = Demo()
# print(d.__doc__)

# class Person:
#     def __init__(self,name,role):
#         self.name = name
#         self.role = role
    
#     def interview(self):
#         print("Interview method....")
#         print(f"Person {self.name} has prepared for the interview..")
#     def job(self):
#         print("Job method...")
#         print(f"Person-{self.name} who had attended the interview, got slected for {self.role}")


# objects with referrence varaibles

# p = Person("Abc","Developer")
# p.interview()
# p.job()
# print("With person2")
# p2 = Person("Anu","Developer")
# p2.job()
# print("Using dict...")
# print(p.__dict__)
# print("Uisng person")




print("Example 2")
class Car:
    def __init__(self):
        self.name = "Punch"
        self.color = "Black"
    def start(self):
        print(f"The car {self.name} -{self.color} has started")
c  = Car()

c.start()
print(c.name)


# print(Car().start)



def student(name,age):
    print(f"Name - {name} : Age - {age}")

student("Anu",25)
print("Hello how are you learning oops.......")

student("Anu",25)

# print(student.name)
print(c.name)



print("With self keyword")

class Demo:
    def __init__(name):
        name.name = "Anu"
        name.age = 25
    def disp(name):
        # self.age = age
        print(f"Name : {name.name} - Age{name.age}")
d = Demo()
d.disp()



# "without constructor"
class Demo:
    def m1(self):
        print(f"Name is {self.name}")
d = Demo()
d.name = "anu"
d.m1()
d1 = Demo()
d1.name = "Anu"
d1.m1()