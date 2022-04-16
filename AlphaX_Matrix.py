'''
Matrix operation using python.
Addition
Subtraction
Multiplication 


Adjoint
Determination 
Transpose
Minor(A)
Co-factor of given element.
Inverse of Matrix

equations

'''




class Matrixdp:
    def __init__(self) -> None:
        mat_ele1 = 0
        mat_ele2 = 0
        mat_ele3 = 0
        mat_res = 0
        mat_multi_res = []
        matrix1 = []
        matrix2 = []
        matrix3 = []
        name1 = 'name'
        name2 = 'name'
        name3 = 'name'
        size = 2
        self.__mat_multi_res = mat_multi_res
        self.__mat_res = mat_res
        self.__mat_ele1 = mat_ele1
        self.__mat_ele2 = mat_ele2
        self.__mat_ele3 = mat_ele3
        self.__matrix1 = matrix1
        self.__matrix2 = matrix2
        self.__matrix3 = matrix3
        self.__matrix_name1 = name1
        self.__matrix_name2 = name2
        self.__matrix_name3 = name3
        self.__size = size

    # Logic for 2 matrices :

    def initalize2(self):
        self.__matrix_name1 = input(f"Enter The Name Of Matrix First: ")
        self.__matrix_name2 = input(f"Enter The Name Of Matrix Second: ")
        self.__size = int(input("Enter the size of both the matrix: "))
        self.__size = self.__size * self.__size
        print("\n")
        for j in range(self.__size):
            self.__mat_ele1 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name1}: "))
            self.__matrix1.append(int(self.__mat_ele1))

        print("\n")
        for j in range(self.__size):
            self.__mat_ele2 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name2}: "))
            self.__matrix2.append(int(self.__mat_ele2))

    def addition2(self):

        print(" ***** Addition *****")
        print(f"{self.__matrix1} + {self.__matrix2}: ")
        for i in range(self.__size):
            self.__mat_res = self.__matrix1[i] + self.__matrix2[i]

            print(f"[{self.__mat_res}]", end=" ")

    def subtraction2(self):

        print(" ***** Subtraction *****")
        print(f"{self.__matrix1} - {self.__matrix2}: ")
        for i in range(self.__size):
            self.__mat_res = self.__matrix1[i] - self.__matrix2[i]
            print(f"[{self.__mat_res}]", end=" ")

    def multiplication2(self):
        print("***** Multiplication *****")
        self.initalize2()
        print(f"{self.__matrix1} X {self.__matrix2}: ")

        if self.__size == 4:
        
            self.__mat_multi_res = [[self.__matrix1[0] * self.__matrix2[0] + self.__matrix1[1] * self.__matrix2[2]], 
                                    [self.__matrix1[0] * self.__matrix2[1] + self.__matrix1[1] * self.__matrix2[3]], 
                                    [self.__matrix1[2] * self.__matrix2[0] + self.__matrix1[3] * self.__matrix2[2]],
                                    [self.__matrix1[2] * self.__matrix2[1] + self.__matrix1[3] * self.__matrix2[3]]]
            print(self.__mat_multi_res)

        elif self.__size == 9:   

            self.__mat_multi_res     =  [[self.__matrix1[0] * self.__matrix2[0] + self.__matrix1[1] * self.__matrix2[3] + self.__matrix1[2] * self.__matrix2[6]], 
                                         [self.__matrix1[0] * self.__matrix2[1] + self.__matrix1[1] * self.__matrix2[4] + self.__matrix1[2] * self.__matrix2[7]], 
                                         [self.__matrix1[0] * self.__matrix2[2] + self.__matrix1[1] * self.__matrix2[5] + self.__matrix1[2] * self.__matrix2[8]],
                                         [self.__matrix1[3] * self.__matrix2[0] + self.__matrix1[4] * self.__matrix2[3] + self.__matrix1[5] * self.__matrix2[6]], 
                                         [self.__matrix1[3] * self.__matrix2[1] + self.__matrix1[4] * self.__matrix2[4] + self.__matrix1[5] * self.__matrix2[7]], 
                                         [self.__matrix1[3] * self.__matrix2[2] + self.__matrix1[4] * self.__matrix2[5] + self.__matrix1[5] * self.__matrix2[8]],
                                         [self.__matrix1[6] * self.__matrix2[0] + self.__matrix1[7] * self.__matrix2[3] + self.__matrix1[8] * self.__matrix2[6]], 
                                         [self.__matrix1[6] * self.__matrix2[1] + self.__matrix1[7] * self.__matrix2[4] + self.__matrix1[8] * self.__matrix2[7]], 
                                         [self.__matrix1[6] * self.__matrix2[2] + self.__matrix1[7] * self.__matrix2[5] + self.__matrix1[8] * self.__matrix2[8]]]
            print(self.__mat_multi_res)        

    def initalize3(self):
        self.__matrix_name1 = input(f"Enter The Name Of First Matrix: ")
        self.__matrix_name2 = input(f"Enter The Name Of Second Matrix: ")
        self.__matrix_name3 = input(f"Enter The Name Of Third Matrix: ")
        self.__size = int(input("Enter the size of all the matrices: "))
        self.__size = self.__size * self.__size
        print("\n")
        for j in range(self.__size):
            self.__mat_ele1 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name1}: "))
            self.__matrix1.append(int(self.__mat_ele1))

        print("\n")
        for j in range(self.__size):
            self.__mat_ele2 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name2}: "))
            self.__matrix2.append(int(self.__mat_ele2))

        print("\n")
        for j in range(self.__size):
            self.__mat_ele3 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name3}: "))
            self.__matrix3.append(int(self.__mat_ele3))
            

    def addition3(self):

        print(" ***** Addition *****")
        print(f"{self.__matrix1} + {self.__matrix2} + {self.__matrix3}: ")
        for i in range(self.__size):
            self.__mat_res = self.__matrix1[i] + \
                self.__matrix2[i] + self.__matrix3[i]
            print(f"[{self.__mat_res}]", end=" ")

    def subtraction3(self):

        print(" ***** Subtraction *****")
        print(f"{self.__matrix1} - {self.__matrix2} - {self.__matrix3}: ")
        for i in range(self.__size):
            self.__mat_res = self.__matrix1[i] - \
                self.__matrix2[i] - self.__matrix3[i]
            print(f"[{self.__mat_res}]", end=" ")

    def interface_arith(self):
        print("\n***** Matrix Arithmetic Operation *****")
        print("\n (1) ***** Addition *****\n (2) ***** Subtraction *****\n (3) ***** Multiplication *****")
        choice = int(input("\nEnter Number Of Matrix Operation: "))
        self.__choice = choice

        print("\n(1) ***** 2 Matrices ***** \n(2) ***** 3 Matrices *****")
        mat_num = int(
            input("\nChoose How many number of matrices going to perform operation: "))
        self.__mat_num = mat_num

        if self.__choice == 1 and self.__mat_num == 1:
            self.initalize2()
            self.addition2()

        elif self.__choice == 2 and self.__mat_num == 1:
            self.initalize2()
            self.subtraction2()

        elif self.__choice == 3 and self.__mat_num == 1:
            self.initalize2()
            self.multiplication2()

        elif self.__choice == 1 and self.__mat_num == 2:
            self.initalize3()
            self.addition3()

        elif self.__choice == 2 and self.__mat_num == 2:
            self.initalize3()
            self.subtraction3()
        
        elif self.__choice == 3:
            self.multiplication2() 

    def adjoint(self):
        print("\n***** Adjoint Of Matrix *****")
        print("\n")
        self.__matrix_name1 = input(f"Enter The Name Of Matrix First: ")
        self.__size = int(input("Enter the size of Matrix: "))
        self.__size = self.__size * self.__size
        print("\n")
        for j in range(self.__size):
            self.__mat_ele1 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name1}: "))
            self.__matrix1.append(int(self.__mat_ele1))

        if self.__size == 4:
            temp = 0
            temp = self.__matrix1[0]
            self.__matrix1[0] = self.__matrix1[3]
            self.__matrix1[3] = temp

            self.__matrix1[1] = self.__matrix1[1] * -1
            self.__matrix1[2] = self.__matrix1[2] * -1
            print(f"Adjoint of 2X2 Matrix {self.__matrix_name1} : {self.__matrix1}")

        elif self.__size == 9:

            self.__matrix_minor = [ self.__matrix1[4] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[5],
                                self.__matrix1[3] * self.__matrix1[8] - self.__matrix1[5] * self.__matrix1[6],
                                self.__matrix1[3] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[4],
                                self.__matrix1[1] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[8] - self.__matrix1[6] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[1],
                                self.__matrix1[1] * self.__matrix1[5] - self.__matrix1[4] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[5] - self.__matrix1[3] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[4] - self.__matrix1[3] * self.__matrix1[1]  ]

            print(f"\nMinor Of Matrix {self.__matrix_name1}:\n{[self.__matrix_minor]}")

            matrix_co_factor = []
            self.__matrix_co_factor = matrix_co_factor

            self.__matrix_co_factor = self.__matrix_minor

            self.__matrix_co_factor[1] *= -1
            self.__matrix_co_factor[3] *= -1
            self.__matrix_co_factor[5] *= -1
            self.__matrix_co_factor[7] *= -1

            print(f"\nCo-Factor Of Matrix {self.__matrix_name1}:\n{self.__matrix_co_factor}")

            self.__matrix1 = self.__matrix_co_factor
            self.__tanspose3 = [self.__matrix1[0] ,self.__matrix1[3] , self.__matrix1[6], self.__matrix1[1] ,self.__matrix1[4] , self.__matrix1[7], self.__matrix1[2] , self.__matrix1[5] , self.__matrix1[8] ]
            print(f"\nAdjoint Of 3X3 Matrix {self.__matrix_name1}:\n{self.__tanspose3}")

          

    def determination(self):
      
        print("***** Determination Of Matrix *****")
        print("\n")
        self.__matrix_name1 = input(f"Enter The Name Of Matrix First: ")
        self.__size = int(input("Enter the size of Matrix: "))
        self.__size = self.__size * self.__size
        print("\n")
        for j in range(self.__size):
            self.__mat_ele1 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name1}: "))
            self.__matrix1.append(int(self.__mat_ele1))

        if self.__size == 4:

            mat_deter2 = 0
            self.__mat_deter2 = mat_deter2

            self.__mat_deter2 = (
                self.__matrix1[0] * self.__matrix1[3]) - (self.__matrix1[1] * self.__matrix1[2])
            print(
                f"\nThe determination of Matrix {self.__matrix_name1}:{self.__mat_deter2}")

        elif self.__size == 9:

            mat_deter3 = 0
            self.__mat_deter3 = mat_deter3
            self.__mat_deter3 = self.__matrix1[0] * (self.__matrix1[4] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[5]) - self.__matrix1[1] * (self.__matrix1[3] * self.__matrix1[8] - self.__matrix1[6] * self.__matrix1[5]) + self.__matrix1[2] * (self.__matrix1[3] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[4])
            print(
                f"\nThe determination of Matrix {self.__matrix_name1}:{self.__mat_deter3}")

    def transpose(self):
        transpose3 = []
        self.__tanspose3 = transpose3
        print("***** Transpose Of Matrix *****")
        print("\n")
        self.__matrix_name1 = input(f"Enter The Name Of Matrix First: ")
        self.__size = int(input("Enter the size of Matrix: "))
        self.__size = self.__size * self.__size
        print("\n")
        for j in range(self.__size):
            self.__mat_ele1 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name1}: "))
            self.__matrix1.append(int(self.__mat_ele1))

        if self.__size == 4:
            temp = self.__matrix1[1]
            self.__matrix1[1] = self.__matrix1[2]
            self.__matrix1[2] = temp
            print(f"Transpose Of Matrix {self.__matrix_name1}:\n{self.__matrix1}")

        elif self.__size == 9:
            self.__tanspose3 = [self.__matrix1[0] ,self.__matrix1[3] , self.__matrix1[6], self.__matrix1[1] ,self.__matrix1[4] , self.__matrix1[7], self.__matrix1[2] , self.__matrix1[5] , self.__matrix1[8] ]
            print(f"Transpose Of Matrix {self.__matrix_name1}:\n{self.__tanspose3}")


    def minor(self):
        matrix_minor = []
        self.__matrix_minor = matrix_minor
        print("***** Minor Of Matrix *****")
        print("\n")
        self.__matrix_name1 = input(f"Enter The Name Of Matrix First: ")
        self.__size = 9
        print("\n")
        for j in range(self.__size):
            self.__mat_ele1 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name1}: "))
            self.__matrix1.append(int(self.__mat_ele1))

        self.__matrix_minor = [ self.__matrix1[4] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[5],
                                self.__matrix1[3] * self.__matrix1[8] - self.__matrix1[5] * self.__matrix1[6],
                                self.__matrix1[3] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[4],
                                self.__matrix1[1] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[8] - self.__matrix1[6] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[1],
                                self.__matrix1[1] * self.__matrix1[5] - self.__matrix1[4] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[5] - self.__matrix1[3] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[4] - self.__matrix1[3] * self.__matrix1[1]  ]

        print(f"Minor Of Matrix {self.__matrix_name1}:\n{[self.__matrix_minor]}")
        
    
    def  co_factor(self):
       
        self.minor()
        matrix_co_factor = []
        self.__matrix_co_factor = matrix_co_factor

        self.__matrix_co_factor = self.__matrix_minor
       
        self.__matrix_co_factor[1] *= -1
        self.__matrix_co_factor[3] *= -1
        self.__matrix_co_factor[5] *= -1
        self.__matrix_co_factor[7] *= -1

        print(f"Co-Factor Of Matrix {self.__matrix_name1}:\n{self.__matrix_co_factor}")
        
    
    def inverse_matrix(self):
        print("***** Inverse Of Matrix *****")
        print("\n")
        self.__matrix_name1 = input(f"Enter The Name Of Matrix First: ")
        self.__size = 9
        print("\n")
        for j in range(self.__size):
            self.__mat_ele1 = int(
                input(f"Enter the {j+1} element of {self.__matrix_name1}: "))
            self.__matrix1.append(int(self.__mat_ele1))
        
        mat_deter3 = 0
        self.__mat_deter3 = mat_deter3
        self.__mat_deter3 = self.__matrix1[0] * (self.__matrix1[4] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[5]) - self.__matrix1[1] * (self.__matrix1[3] * self.__matrix1[8] - self.__matrix1[6] * self.__matrix1[5]) + self.__matrix1[2] * (self.__matrix1[3] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[4])
        print(
            f"\nThe Mode of Matrix {self.__matrix_name1}:{self.__mat_deter3}")

        self.__matrix_minor = [ self.__matrix1[4] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[5],
                                self.__matrix1[3] * self.__matrix1[8] - self.__matrix1[5] * self.__matrix1[6],
                                self.__matrix1[3] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[4],
                                self.__matrix1[1] * self.__matrix1[8] - self.__matrix1[7] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[8] - self.__matrix1[6] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[7] - self.__matrix1[6] * self.__matrix1[1],
                                self.__matrix1[1] * self.__matrix1[5] - self.__matrix1[4] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[5] - self.__matrix1[3] * self.__matrix1[2],
                                self.__matrix1[0] * self.__matrix1[4] - self.__matrix1[3] * self.__matrix1[1]  ]

        print(f"\nMinor Of Matrix {self.__matrix_name1}:\n{[self.__matrix_minor]}")

        self.__matrix_co_factor = self.__matrix_minor
       
        self.__matrix_co_factor[1] *= -1
        self.__matrix_co_factor[3] *= -1
        self.__matrix_co_factor[5] *= -1
        self.__matrix_co_factor[7] *= -1

        print(f"\nCo-Factor Of Matrix {self.__matrix_name1}:\n{self.__matrix_co_factor}")

        
        self.__matrix1 = self.__matrix_co_factor
        self.__tanspose3 = [self.__matrix1[0] ,self.__matrix1[3] , self.__matrix1[6], self.__matrix1[1] ,self.__matrix1[4] , self.__matrix1[7], self.__matrix1[2] , self.__matrix1[5] , self.__matrix1[8] ]
        print(f"\nTranspose Of Co-Factor {self.__matrix_name1}:\n{self.__tanspose3}")

        print(f'''
                Inverse of {self.__matrix_name1} : 1
                            --------    X    {self.__tanspose3}
                               {self.__mat_deter3}
        ''')




d = Matrixdp()

print("***** Matrix *****")
print("\n***** (1) Arithmetic Operation Of Matrix *****")
print("***** (2) Adjoint Of Singular Matrix *****")
print("***** (3) Determination Of Matrix *****")
print("***** (4) Minor Of Matrix *****")
print("***** (5) Co-Factor Of Matrix *****")
print("***** (6) Transpose Of Matrix ******")
print("***** (7) Inverse Of Matrix *****")
select = int(input("Select Your Choice: "))

if select == 1:
    d.interface_arith()

elif select == 2:
    d.adjoint()

elif select == 3:
    d.determination()

elif select == 4:
    d.minor()
    
elif select == 5:
    d.co_factor()

elif select == 6:
    d.transpose()

elif select == 7:
    d.inverse_matrix()