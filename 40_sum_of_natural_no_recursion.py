def natural_no(n):
    if n<=1:
        return n
    else:
        return n + natural_no(n-1)

num = int(input("Enter any number")) 

sum_no = natural_no(num)
print(sum_no)

