
a = [1,2,3,4,5,5,6,6,7,8,9,5,7,6,2,8,9,10,10,2]
b = []

for i in a:

    if i not in b:
        b.append(i)
    
print(b)