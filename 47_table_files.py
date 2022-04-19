for i in range(2 , 20):
    with open(f'table file{i}.txt', 'w') as f:
        for j in range(1,11):
            table = f.write(f'{i}X{j}={i*j}\n')
    


