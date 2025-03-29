# Площадь квадрата

import math

def square(size):
    return math.ceil(size ** 2)

try:
    input_size = float(input("Задайте длину стороны квадрата: "))
    print("Площадь квадрата -", square(input_size)) 

except ValueError:
    print("Пожалуйста, введите число c разделителем дробной части '.'")
