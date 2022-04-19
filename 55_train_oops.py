class Train:
   
    def __init__(self,trainName,trainSeats,trainFair):
        self.name = trainName
        self.seats = trainSeats
        self.fair = trainFair

    def book(self):
        if self.seats>0:
            print("Your ticket is booked!!!")
            self.seats = self.seats-1
        
        else:
            print("Sorry this train is has no seat try in another train")

    def getInfo(self):
        print(f"Train: {self.name} \nSeats: {self.seats} \nTotal Fair: Rs. {self.fair} ")

intercity = Train("Intercity Express",10,30)

intercity.book()
intercity.getInfo()