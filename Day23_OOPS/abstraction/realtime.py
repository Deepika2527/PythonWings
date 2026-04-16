from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdrawl(self,amount):
        pass
    def check_bal(self):
        print(f"The Balance {self.balance}")
class Sbi(Bank):
    def __init__(self,balance,):
        self.balance = balance
    def deposit(self, amount):
        if amount >1000:
            self.balance += amount
            print("After Depoisted balcnce is❤️😎", self.balance)
    def withdrawl(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print("After Withdrawl your current balcnce is", self.balance)
        else:
            print("INvalid bala....")

s = Sbi(10000)
s.check_bal()
s.deposit(5000)
s.withdrawl(3000)
        
    


        

        
        


