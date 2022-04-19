d1 = [1,2,24,23,30]

print("Here we are sorting our list with the use of .sort() function")

d1.sort()

print("The sorted list of d1 is: ",d1)

print(d1)

print("here we are adding an new element at the end of the list using .append() function")

d1.append(50)

print(d1)

print("Here we are adding an new element at any index with the use of .insert()")

d1.insert(2,51)

print(d1)

print(".pop() will delete an element at index and return its value")

d1.pop(2)

print(d1)

print(".remove() will remove the value from the list")

d1.remove(50)

print(d1)

print("Here we are update our list in reverse order with the use of .reverse() function")

d1.reverse()