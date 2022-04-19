a = [ ]
b = [ ]

print("Enter the element of Matrix A")
for i in range(9):
    eleA = int(input(f"{i} element Matrix A: "))
    a.append(eleA)

print("Enter the element of Matrix B")
for i in range(9):
    eleB = int(input(f"{i} element Matrix B: "))
    b.append(eleB)

for i in  a ,b:
    print(i)

sum_mat = 0
for i in range(0,9):

    sum_mat = a[i] + b[i]
    print(f"[{sum_mat}]\t",end=" ")

