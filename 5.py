import random

n = 3
array  = [[random.randint(-250,250) for _ in range(n)] for _ in range(n)]
for i in array:
    print(i)

rez = 0
for i in range(n):
    rez += array[i][i]
    rez += array[n-i-1][i]
print("Сумма элементов расположенных на главной и побочной диагоналях",rez)