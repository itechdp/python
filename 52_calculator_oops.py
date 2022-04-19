class Calculator:

    def __init__(self,num):
        self.number = num
    
    def square(self):
        print(f"The square of the {self.number} is {self.number **2}")

    def cube(self):
        print(f"The cube of the {self.number} is {self.number **3}")

    def squareRoot(self):
        print(f"The square root of the {self.number} is {self.number **0.5}")


a = Calculator(25)   
a.square()
a.cube()
a.squareRoot()


