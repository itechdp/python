class Complex:

    def __init__(self, r=0.0, i=0.0):
        self.__real = r
        self.__imag = i

    def __eq__(self,other):
        if self.__real == other.__real and self.__imag == other.__imag:
            return True
        else:
            return False

c1 = Complex(1.1 , 0.2)
c2 = Complex(2.1, 0.4)
c3 = c1

if c1 == c2:
    print("Attributes of c1 and c2 are same")

else:
    print("Attributes  of C1 and c2 are different")

if type(c1) == type(c3):
    print("C1 and C3 have same type")

else:
    print("C1 and C3 have different different type")

if c1 is c3:
    print("Both are pointing a same object")
    
else:
    print("Both are printing different object")
