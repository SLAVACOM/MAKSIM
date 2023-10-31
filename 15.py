ARRAY_SIZE = 2
MIN_ELEMENT_ARRAY = -100
MAX_ELEMENT_ARRAY = 100

import random

def genArray():
    matrix = []
    for i in range(ARRAY_SIZE):
        array = []
        for j in range(ARRAY_SIZE):
            array.append(random.randint(MIN_ELEMENT_ARRAY,MAX_ELEMENT_ARRAY+1))
        matrix.append(array)
    print("Двумерный массив:")
    for i in range(ARRAY_SIZE):
        print(*matrix[i])
    return matrix

def calculate(matrix):
    main_diagonal = 0
    side_diagonal = 0
    for i in range(ARRAY_SIZE):
        main_diagonal+=matrix[i][i]
        side_diagonal+=matrix[ARRAY_SIZE-i-1][i]
    print(f"Сумма главной диагонали: {main_diagonal}\n"
          f"Сумма побочной диагонали: {side_diagonal}")
if __name__ == "__main__":
    matrix = genArray()
    calculate(matrix)