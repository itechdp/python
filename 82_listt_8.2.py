
odd = [1,3,5,7,9]
print(odd)

even = [2,4,6,8,10]
print(even)

odd = odd + even
odd.sort()
odd.append('11')
print(odd)

odd = [11,17,29] + odd
print(odd)

leng = len(odd)

odd[leng-3:leng] = [100,200,300]

print(odd)

odd[:] = []
print(odd)

del odd

contact = {}

name = input("enter name:")
no  = input("no:")

contact = contact({name : no})
print(contact)