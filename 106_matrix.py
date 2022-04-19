a = [

    1,  2,  3,
    4,  5,  6,
    7,  8,  9
]

b = [

    1,  2,  3,
    4,  5,  6,
    7,  8,  9
]

sum_mat = 0

print(f"\n{a} + {b}:\n")
for i in range(0,9):

    sum_mat = a[i] + b[i]
    print(f"[{sum_mat}]\t",end=" ")

print(f"\n\n{a} - {b}:")
print("\n")
for j in range(0,9):

    sum_mat = a[j] - b[j]
    print(f"[{sum_mat}]\t",end=" ")

print(f"\n\n{a} * {b}:")
print("\n")
for k in range(0,9):

    sum_mat = a[k] * b[k]
    print(f"[{sum_mat}]\t",end=" ")

  