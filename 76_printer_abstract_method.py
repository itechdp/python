
from abc import abstractclassmethod


class Printer:
    def __init__(self,n) :
        self.__n = n
    
    @abstractclassmethod
    def print(self,docname):
        pass

class Laserprinter(Printer):
    def __init__(self, n) :
        super().__init__(n)
    
    def print(self,docname):
        print('>>LasePrinter.print')
        print('Tyring to print:',docname)

class Inkjetprinter(Printer):
    def __init__(self, n) -> None:
        super().__init__(n)

    def print(self,docname):
        print('>>InkjetPrinter.print')
        print('Tyring to print:',docname)

p = Laserprinter('Laserjet 1100')
p.print('hello1.pdf')

p = Inkjetprinter('IBM 2140')
p.print('hello.pdf')