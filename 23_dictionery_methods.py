a = {

    "dhrumil": "loves coding",
    "krishna": "loves football"
}

# use this syntax to get the value of the entered key in the print function

print(a["dhrumil"])

# .items() used to get the key values of the dictionary

print(a.items())

# .keys() to get the list of keys of the dictionary

print(a.keys())

# .update() used to update the list as shown in the below lines of codes

a.update({"mummy": "loves cooking"})

print(a)

# .get() Get the value of the entered key without throwing the error

print(a.get("mummy"))


dict1 = {
    
    1:"hello",
    2:"world",
    "dhrumil": 23
    
}


print(dict1)

#used to get the values of the dictionary
print(dict1.values())

#used to update the dictionary or append the list taking argument in {} braces and taking key-value pairs 
dict1.update({'rian':30})
print(dict1)

#used to delete the last inserted key-value pair from the dictionary
dict1.popitem()
print(dict1)

#used to remove the particular dictionary element taking argument as an index value
dict1.pop(1)
print(dict1)
