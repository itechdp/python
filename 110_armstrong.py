def power(x, y):
      
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
          
    return x * power(x, y // 2) * power(x, y // 2)

def order(num):
    n = 0
    while(num != 0):
        n+=1
        num//=10
    
    return n

def isarmstrong(num): 

    n = order(num)
    temp = num
    sum1 = 0 
    while (temp != 0): 
        
        r = num % 10
        sum1 = sum1 + pow(r,n)
        temp //= 10

    return (sum1 == num)



num = int(input("Enter a number: "))
print(isarmstrong(num))
