import random

a = []

for i in range(21):
    num = random.randint(0,50)
    a.append(num)

print(a)

ind = int(input("Enter any number of those and find the index of occurance: "))
ind2 = a.index(ind)
print(f"Entered number is occured on index: {ind2}")
