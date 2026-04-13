class Student():
    def __init__(self,name,__marks):
        self.name = name
        self.__marks = __marks
    def Disp(self):
        print("Name :", self.name)
        print("Marks :", self.__marks)
    
s = Student("Anu",99)
s.Disp()
print(s.name)
# print(s.__marks)

print(s._Student__marks) 




print(".........................getter and getter...............")

class Bank():
    def __init__(self,name,accn,__bal):
        self.name = name
        self.accn = accn
        self.__bal = __bal
    def display(self):
        print("Name :", self.name)
        print("Account Number :", self.accn)
        # print("Diplay Bal", self.__bal)
    def get_balance(self):
        return self.__bal 
    def set_bal(self,v):
        if 0 <v >10 :
            self.__bal += v
            # print(self.__bal)
b = Bank("Anu",1010,5000)
b.display()
print(b.get_balance())
b.set_bal(1000)
print(b.get_balance())
b.set_bal(3)
print(b.get_balance())
b.set_bal(11)
print(b.get_balance())
