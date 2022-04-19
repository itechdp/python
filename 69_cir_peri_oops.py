# Equilateral triangle : P = 3 x a
# Scalene Triangle :	P = a + b + c
# Square	:	P = 4 x a
# Rectangle : P = 2 ( a + b )
# Quadrilateral : P = a + b + c + d
# Regular Pentagon : P = 5 x a
# Regular Hexagon : P = 6 x a
# Regular Octagon : P = 8 x a
#Circumference : 2 x pie x r


class Calculate:
    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0,r=0.0,pie=3.14):
        print("***** Find The Perimeter Of Any Shape Here *****\n")
        a = float(input("Enter The Value of A(side):"))
        b = float(input("Enter The Value of B(side):"))
        c = float(input("Enter The Value of C(side):"))
        d = float(input("Enter The Value of D(side):"))
        r = float(input("Enter The Value of Radius:"))

        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__r = r
        self.__pie = pie
    
    def EquTri(self):
        return self.__a * 3
    
    def ScaleneTri(self):
        return self.__a + self.__b + self.__c

    def square(self):
        return 4 * self.__a

    def rec(self):
        return 2*(self.__a + self.__b)
    
    def quadri(self):
        return self.__a + self.__b + self.__c + self.__d
    
    def pentagon(self):
        return 5 * self.__a
    
    def hexagon(self):
        return 6 * self.__a
    
    def octagon(self):
        return 8 * self.__a
    
    def circumCircle(self):
        return 2 * self.__pie * self.__r


    @property
    def condtion(self):

        choice2 = int(input('''
To see the perimeter of perticular shape(1)
To see the perimeter of all shapes (2)\nYour Choice:'''))


        if choice2 == 1:
            choice = int(input('''
***** Make Choice And Find The Perimeter Of Any Shape *****

Equilateral triangle(1)
Scalene Triangle(2)
Square(3)
Rectangle(4)
Quadrilateral(5)
Regular Pentagon(6)
Regular Hexagon(7)                             
Regular Octagon(8)
Circumfrence Of Circle(9)
Your Choice: '''))
            if choice == 1:
                print(f"The Perimeter of Equilateral triangle is: {self.EquTri()}")
            elif choice == 2:
                print(f"The Perimeter of Scalene Triangle is: {self.ScaleneTri()}")
            elif choice == 3:
                print(f"The Perimeter of Square is: {self.square()}")
            elif choice == 4:
                print(f"The Perimeter of Rectangle is: {self.rec()}")
            elif choice == 5:
                print(f"The Perimeter of Quadrilateral is: {self.quadri()}")
            elif choice == 6:
                print(f"The Perimeter of Regular Pentagon is: {self.pentagon()}")
            elif choice == 7:
                print(f"The Perimeter of Regular Hexagon is: {self.hexagon()}")
            elif choice == 8:
                print(f"The Perimeter of Regular Octagon is: {self.octagon()}")
            elif choice == 9:
                print(f"The Circumference of circle is: {self.circumCircle()}")
            else:
                print("Invalid Choice!!!")
            
        if choice2 == 2:
            print(f"\nThe Perimeter of Equilateral triangle is: {self.EquTri()}")

            print(f"The Perimeter of Scalene Triangle is: {self.ScaleneTri()}")

            print(f"The Perimeter of Square is: {self.square()}")
                
            print(f"The Perimeter of Rectangle is: {self.rec()}")

            print(f"The Perimeter of Quadrilateral is: {self.quadri()}")
                
            print(f"The Perimeter of Regular Pentagon is: {self.pentagon()}")
            
            print(f"The Perimeter of Regular Hexagon is: {self.hexagon()}")
            
            print(f"The Perimeter of Regular Octagon is: {self.octagon()}")
            
            print(f"The Circumference of circle is: {self.circumCircle()}")
            

v1 = Calculate()
v1.condtion

v2 = Calculate()
v1.condtion