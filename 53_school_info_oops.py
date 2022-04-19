from unicodedata import name


class SchoolInfo:
    name = "name"
    standard = "std"

    def getInfo(self):
        print(f"The name of {self.name} studying in {self.standard}") 

dhrumil = SchoolInfo()
fannie = SchoolInfo()

dhrumil.name = "dhrumil piyush patel"
dhrumil.standard = "10 B"
fannie.name = "Fannie tony k "
fannie.standard = "10 B"

dhrumil.getInfo()
fannie.getInfo()