import random

s = '-=+!@#%*' # Набор символов
s_count = len(s) # кол-во символов в наборе
n = 5; m = 7 # размеры двумерного массива
def random_symbol(): # ф-я возвращает какой то сивол из набора
    return s[random.randint(0,s_count-1)]

array = [ [random_symbol() for i in range(n)] for j in range(m)]# Создаем изаролняем двумерный масив с помощью генераторов

for i in range(m):# Вывод массива
    print(array[i])

for i in range(len(array)):# Вывод количество символов '+'
    print(f"В строке №{i+1} количество символов '+' равно {array[i].count('+')}")


