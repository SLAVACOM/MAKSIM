# Параметры которые можно изменять
MATRIX_SIZE = 10  # Размер матрицы
MIN_ELEMENT_ARRAY = -100  # Миниммальное число которое может быть в матрице
MAX_ELEMENT_ARRAY = 100  # Максимальное число которое может быть в матрице

import random


def genArray():  # Ф-я создаёт двумерный массив и заполняет его
    matrix = []
    for i in range(MATRIX_SIZE):
        array = []
        for j in range(MATRIX_SIZE):
            array.append(random.randint(MIN_ELEMENT_ARRAY, MAX_ELEMENT_ARRAY + 1))
        matrix.append(array)
    print("Двумерный массив:")
    for i in range(MATRIX_SIZE):
        print(*matrix[i])
    return matrix


def calculate(matrix):
    main_diagonal = 0
    side_diagonal = 0
    for i in range(MATRIX_SIZE):
        main_diagonal += matrix[i][i]  # Считаем главную диагональ
        side_diagonal += matrix[MATRIX_SIZE - i - 1][i]  # Считаем побочную диагональ
    print(f"Сумма главной диагонали: {main_diagonal}\n"
          f"Сумма побочной диагонали: {side_diagonal}")


if __name__ == "__main__":
    matrix = genArray()
    calculate(matrix)
