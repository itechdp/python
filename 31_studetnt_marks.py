m1 = float(input("Enter your Computer Marks:"))
m2 = float(input("Enter your maths marks: "))
m3 = float(input("Enter your physics marks: "))


avg = (m1+m2+m3)/3

if(avg>=40):
    print("Your are pass")
    print(avg)

elif(avg<=33):
    print("Your are fail")
    print(avg)

