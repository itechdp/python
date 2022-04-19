
class Shape:
    pass

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

s = Shape()
c = Circle()

print(isinstance(s,Shape))
print(isinstance(c,Circle))
print(isinstance(s,Rectangle))
print(issubclass(Circle , Shape))
print(issubclass(Rectangle , Shape))
