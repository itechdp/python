class Fruit:

    count = 0
    def __init__(self,size = "", color = " ",name = "."):
        self.name = name
        self.color = color 
        self.size = size 
        Fruit.count +=1
    
    def display():
        print(Fruit.count)
    
apple = Fruit(10,"red","apple")
banana = Fruit(11,"yellow","banana")

Fruit.display() # Calling a class method using classname.methodname
print(Fruit.count) # Printing a class instance