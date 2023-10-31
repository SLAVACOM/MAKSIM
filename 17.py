# Параметры которые можно изменять
ARRAY_LENGTH = 10  # Размер массива
MIN_ELEMENT_ARRAY = -100  # Миниммальное число которое может быть в массиве
MAX_ELEMENT_ARRAY = 100  # Максимальное число которое может быть в массиве

import random
def genArray(): #Ф-я создаёт массив и заполняет его рандомными числами
    array = [] #Создаётся массив
    for i in range(ARRAY_LENGTH): #Заполняется массив
        array.append(random.randint(MIN_ELEMENT_ARRAY,MAX_ELEMENT_ARRAY+1))
    print(f"Массив: {array}.") #выводит массив
    return array

def calculateArray(array):#Ф-ия
    sum_positnive = 0
    product_negative = 1
    for i in array:
        if i < 0: # Если элемент отрицательный
            product_negative *= i
        else: # Если элемент положительный
            sum_positnive += i
    if abs(product_negative) > sum_positnive:
        print("Абсолютная величина произведения отрицательных элементов больше чем сумма положительных элементов.")
    elif abs(product_negative) == sum_positnive:
        print("Абсолютная величина произведения отрицательных элементов равна сумме положительных элементов.")
    else:
        print("Сумма положительных элементов больше чем абсолютная величина произведения отрицательных элементов")


if __name__ == "__main__":
    array = genArray()
    calculateArray(array)