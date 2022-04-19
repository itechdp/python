
from email.mime import base
from operator import index


class Base:
    def __init__(self) -> None:
        self.i = 10
        self._a = 3.14 
        self.__s = 'Hello'

    def display(self):
        print(self.i , self._a , self.__s)

class Derived(Base):
    def __init__(self) -> None:
        super().__init__()
        self.i = 100
        self._a = 31.44
        self.__s = 'Good morning'
        self.j = 200 
        self._b = 6.28
        self.__ss = "hi"

    def display(self):
        super().display()
        print(self.i , self._a , self.__s)
        print(self.j , self._b , self.__ss)

bobj = Base()
bobj.display()
print(bobj.i)
print(bobj._a)

dobj = Derived()
dobj.display()
print(dobj.i)
print(dobj._a)
print(dobj.j)
print(dobj._b)

print(dir(object))
print(dir(index))
