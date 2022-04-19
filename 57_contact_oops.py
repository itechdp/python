from operator import contains


class Contact:
    
    def __init__(self,name,no):
        self.no = no
        self.name = name

    def contactInfo(self):
        print(f"Name:{self.name}\nContact NO:{self.no}")
        print("**********")
    
rina = Contact("Mummy","884412345")
fannie = Contact("My love","9879609710")
dhrumil = Contact("Me","7802032338")

rina.contactInfo()
fannie.contactInfo()
dhrumil.contactInfo()
