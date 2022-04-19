from abc import abstractclassmethod


class Character:

    @abstractclassmethod
    def patriotism():
        pass

class Actor:

    def style(self):
        print('>>Actor.style')

class person(Character,Actor):
    
    def do_acting(self):
        print('>> Person.doacting')
    
    def style(self):
        print('>> Person.Style')
    
    def patriotism(self):
        print('>> Person.patriotism')

p = person()
p.do_acting()
p.style()
p.patriotism()

