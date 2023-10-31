ARRAY_LENGTH = 10
MIN_ELEMENT_ARRAY = -100
MAX_ELEMENT_ARRAY = 100

import random
def genArray():
    array = []
    for i in range(ARRAY_LENGTH):
        array.append(random.randint(MIN_ELEMENT_ARRAY,MAX_ELEMENT_ARRAY+1))
    print(f"Массив: {array}.")
    return array

def calculateArray(array):
    sum_positnive = 0
    product_negative = 1
    for i in array:
        if i < 0:
            product_negative *= i
        else:
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