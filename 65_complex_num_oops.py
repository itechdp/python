
class ComplexNum:
    def __init__(self, r=0, i=0, r2=0, i2=0):
        sumcompr = 0
        sumcompi = 0
        r = int(input("Enter a real part:"))
        r2 = int(input("Enter a real part:"))
        i = int(input("Enter Imaginary Part:"))
        i2 = int(input("Enter Imaginary Part:"))
        self.__sumcompr = sumcompr
        self.__sumcompi = sumcompi
        self.__real = r
        self.__imag = i
        self.__real2 = r2
        self.__imag2 = i2

    # @property
    def addtionComplex(self):
        self.__sumcompr = self.__real + self.__real2
        self.__sumcompi = self.__imag + self.__imag2
        print(f"{self.__sumcompr} + {self.__sumcompi}i")

    # @property
    def subComplex(self):
        self.__sumcompr = self.__real - self.__real2
        self.__sumcompi = self.__imag - self.__imag2
        print(f"{self.__sumcompr} - {self.__sumcompi}i")

    # @property
    def multiComplex(self):
        self.__sumcompr = self.__real * self.__real2
        self.__sumcompi = self.__imag * self.__imag2
        print(f"{self.__sumcompr} * {self.__sumcompi}i")

    # @property
    def divideComplex(self):
        self.__sumcompr = self.__real / self.__real2
        self.__sumcompi = self.__imag / self.__imag2
        print(f"{self.__sumcompr} / {self.__sumcompi}i")


c1 = ComplexNum()
c1.addtionComplex()



