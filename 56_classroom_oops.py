class Classroom:
    def __init__(self,name,rollno,std):
        self.name = name
        self.rollno = rollno
        self.std = std
    
    def getInfo(self):
        print(f"Student Name:{self.name}\nRollNO. :{self.rollno}\nStandard:{self.std}")
        print("**********")

    
dhrumil = Classroom("dhrumil","T1121CE2330","10")
fannie = Classroom("Fannie","T1121CE3023","10")
rian = Classroom("Rian","T1121CE242","10")

dhrumil.getInfo()
fannie.getInfo()
rian.getInfo()
        