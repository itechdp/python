class Base:
    def __method(self):
        print('In Base.__method')
    
    def func(self):
        self.__method()

class Derived(Base):
    def __method(self):
        print('In Derived.__method')
    

b = Base()
b.func()

d = Derived()
d.func()