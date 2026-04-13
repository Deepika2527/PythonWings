# class Studnet():
#     def __init__(self,marks):
#         self.marks = marks
#     def display(self):
#         print(f"Student marks are {self.marks}")
# s = Studnet(90)
# s.display()
# print(s.marks)
# s.marks = -90
# s.display()

# print("--------------------------------------")

# print("Using Protected....")
# class Student():
#     def __init__(self,_marks):
#         self._marks = _marks
#     def get_marks(self):
#         print(f"Marks are {self._marks}")
# s = Student(80)
# s.get_marks()
# print(s._marks)
# s._marks = -90
# print(s._marks)




class Studnet():
    def __init__(self,_m):
        self._m = _m
    def display_marks(self):
        print("Display Marks :", self._m)
class UpdateMarks(Studnet):
    # def __ini__(self,v):
    #     self.v = v
    def updated_marks(self,v):
        self.v = v
        self._m = self.v
        print(f"The Marks are {self._m}")
u = UpdateMarks(100)
u.display_marks()
u.updated_marks(90)
# u.updated_marks()

