fav = {}
a = input("enter your fav language")
b = input("enter your fav language")
c = input("enter your fav language")
d = input("enter your fav language")

fav["dhrumil"] = a
fav["rian"] = b
fav["fannie"] = c
fav["krishna"] = d

print(type(fav))

print(fav.items())

when the key are with the same name it will overwrite the value of a key

to prove that un-comment below code

fav = {}
a = input("enter your fav language")
b = input("enter your fav language")
c = input("enter your fav language")
d = input("enter your fav language")

fav["dhrumil"] = a
fav["fannie"] = b
fav["fannie"] = c
fav["krishna"] = d

print(type(fav))

print(fav.items())
