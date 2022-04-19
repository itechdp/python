from audioop import add
from functools import total_ordering


class Addition:

    n = 100
    n2 = 200

    @property
    def total(self):
        return self.n + self.n2 

        

num = Addition()

print(num.total)

class Balence: 

    
    def __add__(self,cbal,abal):

        self.cbal = cbal
        self.abal = abal
       
        return self.abal + self.cbal
        
dhrumil = Balence()
dhrumil.cbal = 500
dhrumil.abal = int(input("Enter the amount of money deposit: "))

print(dhrumil.cbal + dhrumil.abal)
