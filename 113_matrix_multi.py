a = [[0,1] , [2,3]]
b = [[0,1] , [2,3]]
c = [[0,0] , [0,0]]

'''
    0   1         0   2         0+2 0+3       2  3
             X              =   0+6 2+9     = 6 11
    2   3         1   3

'''
for m in range(len(a)): 
    print('m:',a[m])   
    for n in range(len(b[0])):  
        print('n:',b[n])  
        for o in range(len(b)):    
            print('o:',b[o])
            c[m][n] += a[m][o] * b[o][n]
            
for rs in c:
    print(rs)

i = [[1,2] , [4,5]]
j = [[1,2] , [4,5]]
k = [[1,2] , [4,5]]
r = [[0,0] , [0,0]]

result_mat = 0

for x in range(len(i)):
    for y in range(len(j[0])):
        for z in range(len(k[0])):
            for d in range(len(j)):
                for f in range(len(k)):
                    result_mat[i][j][k] += i[x][y][d]* j[y][k][k] * k[x][d][f] 

print(result_mat)