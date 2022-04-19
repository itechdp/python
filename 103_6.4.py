b = '2330'
i = 0
while b:
    i = i*2+(ord(b[0])-ord(('0')))
    b = b[1:]
print("Value:",str(i))