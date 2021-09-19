
class Employee():

    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property 
    def fullName(self):
        return f"{self.first} {self.last}"
    
    def payRaise(self):
        self.pay = self.pay * self.raise_amount
    
    def test(self,a,b):
        return a+b