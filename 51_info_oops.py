class Programmer:
    company = "Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The {self.name} is working on {self.product} ")




dhrumil = Programmer("dhrumil","gta7")  
fannie = Programmer("fannie","beauty")
dhrumil.getInfo()
fannie.getInfo()