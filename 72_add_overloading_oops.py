class Addition:
    def __init__(self,a=0,b=0):
        a = int(input("Enter the value of A:"))
        b = int(input("Enter the value of B:"))
        self.__a = a
        self.__b = b
    
    def __add__(self,other):
        z = self.__a + other.__a + self.__b + other.__b
        return z
c = Addition()
c1 = Addition()

c3 = c + c1
print(c3)




        