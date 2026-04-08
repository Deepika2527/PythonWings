# class Mother:
#     def get_skill(self):
#         print("Mother can Dance very well....")
# class Father:
#     def get_talent(self):
#         print("Father can paint very well....")
# class Child(Mother,Father):
#     def get_hobby(self):
#         print("Child knows both Dancing and painting and he also knows swimming")
# c = Child()
# c.get_hobby()
# c.get_skill()
# c.get_talent()
# print(Child.mro())

# class Mother:
#     def __init__(self,skill):
#         self.skill = skill
#     def mother_skill(self):
#         print(f"Mother knows {self.skill}")
# class Father:
#     def __init__(self,hobby):
#         self.hobby = hobby
#     def father_hobby(self):
#         print(f"Father's hobby {self.hobby}")
# class Child(Mother,Father):
#     def __init__(self,skill,hobby,talent):
#         Mother.__init__(self,skill)
#         Father.__init__(self,hobby)
#         self.talent = talent
#     def child_talent(self):
#         print(f"The Child got {self.skill} from mother, {self.hobby} from father and also the child knows {self.talent}")
# c = Child("Signing","Painting","Swimming")
# c.child_talent()
# c.mother_skill()
# c.father_hobby()



class A:
    def show_data(self):
        print("the data is showing -A")
class B:
    def show_data(self):
        print("the data is showing -B")
# class C(A,B):
#     pass
class D(B,A):
    pass

# c = C()
# c.show_data()
d = D()
d.show_data()