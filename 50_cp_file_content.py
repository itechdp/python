import os

with open('sample.txt') as f:
    copy = f.read()

with open('newsample.txt','w') as f:
    paste = f.write(copy)

os.remove("sample.txt") #os.remove is used to remove the file in the directory