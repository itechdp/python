class ArithmeticOpt:
    def __init__(self , n1 = 0 , n2 = 0):
        self.__n1 = n1 
        self.__n2 = n2
    
    def Add(self):
        return self.__n1 + self.__n2
    
    def sub(self):
        return self.__n1 - self.__n2
    
    def multi(self):
        return self.__n1 * self.__n2
    

num1 = ArithmeticOpt(2 , 5)

print(num1.Add())
print(num1.sub())
print(num1.multi())
