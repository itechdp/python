def remove_strip(string,word):
    newstring = string.replace(word,"")
    return newstring.strip()

name = "     dhrumil is a good boy       "

newstr = remove_strip(name,"dhrumil")
print(newstr)
