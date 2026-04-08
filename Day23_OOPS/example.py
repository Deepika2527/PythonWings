class Employee:
    def work(self):
        print("Employee has work")
class Developer:
    def work(self):
        print("Employee has work")
class Tester:
    def work(self):
        print("Employee has some work")
t = Tester()
d = Developer()
e = Employee()
t.work()
d.work()
e.work()

print("---------with inheritance-----------------")
class A:
    def work(self):
        print("Employee has some work")
class B(A):
    pass
class C(A):
    pass
c = C()
c.work()
b = B()
b.work()


