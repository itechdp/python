# Solid Shape	Property	Volume Formula (Cubic Units)
# Cube	Face – square (6) vertices – 8 Edges – 12	a3
# Cuboid	Face – Rectangle (6) vertices – 8 Edges – 12	l × b × h
# Sphere	Curved surface = 1 Edges = 0 Vertices = 0	(4/3)πr3
# Cylinder	Flat Surface = 2 Curved Surface = 1 Face = 3 Edges =2 Vertices =0	πr2h

class Areasolid:

    def __init__(self, l=0, h=0, a=0, b=0, r=0, pie=3.14):

        a = int(input("Enter of value the of A: "))
        l = int(input("Enter the length: "))
        b = int(input("Enter the breath: "))
        h = int(input("Enter the height: "))
    
        self.__pie = pie 
        self.__l = l
        self.__h = h
        self.__a = a
        self.__b = b
        self.__r = r
       
    def cube(self):
        return self.__a * self.__a * self.__a
    
    def cuboid(self):
        return self.__l * self.__b * self.__h

    def sphere(self):
        return (4/3)* self.__pie * self.__r
    
    def cylinder(self):
        return self.__pie * self.__h * 2 * self.__h

    @property
    def Condition(self):
        choice = int(input("Cube(1)\nCuboid(2)\nSphere(3)\nCylinder(4)"))

        if choice == 1:
            print(f"The Area of cube is: {self.cube()}")
        elif choice == 2:
            print(f"The Area of cuboid is: {self.cuboid()}")
        elif choice == 3:
            print(f"The Area of sphere is: {self.sphere()}")
        elif choice == 4:
            print(f"The Area of cube is: {self.cylinder()}")
        else:
            print("Invalid choice!!!")

c1 = Areasolid()
c1.Condition