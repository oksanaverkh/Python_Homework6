# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


## List comprehension were used
# New decision of the task: Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
import random
from math import fabs

os.system('cls')


def check_int():
    num = int(input('Enter list length: '))
    while not num >=1:
        print('Wrong number, try again')
        num = int(input('Enter list length: '))
    return int(num)
def check_float():
    lim = float(input('Enter list length: '))
    while not lim >=1:
        print('Wrong number, try again')
        lim = float(input('Enter list length: '))
    return float(lim)

def main():
    n, limit = check_int(), check_float()
    my_list = [round(random.uniform(-limit, limit),3) for _ in range(n)]
    fractional_parts_list = list(map(lambda x: round(fabs(x)%1,3), my_list))
    print('List of real numbers:', my_list)
    print('List of fractional parts:', fractional_parts_list)

    max = 0
    min =1
    for _, elem in enumerate(fractional_parts_list):
        if elem > max:
            max =elem
        elif elem < min:
            min = elem
    print()
    print(f'Max fractional part value of elements = {round(max,3)}')
    print(f'Min fractional part value of elements = {round(min,3)}')
    diff = max - min
    print()
    print(f'Difference between max and min values = {round(diff,3)}')

if __name__ == '__main__':
    main()





# # Previous decision
# import os
# import random
# from math import fabs
# from sys import maxsize
# os.system('cls')

# n = int(input('Enter list length: '))
# limit = float(input('Enter list limit value: '))

# if n <= 0 or limit <= 0:
#     print('Enter another value')

# else:
#     def list_creation(n, limit):
#         new_list = []
#         for _ in range(n):
#             new_list.append(round(random.uniform(-limit, limit), 3))
#         return new_list

#     def fractional_part_diff(new_list):
#         fractional_parts_list = []
#         max = 0
#         min = 1
#         for i in range(len(new_list)):
#             fractional_parts_list.append((fabs(new_list[i]) % 1))
#             if fractional_parts_list[i] > max:
#                 max =fractional_parts_list[i]
#             elif fractional_parts_list[i] < min:
#                 min = fractional_parts_list[i]
#         print(fractional_parts_list) 
#         print(f'Max fractional part value of elements = {round(max,3)}')
#         print(f'Min fractional part value of elements = {round(min,3)}')
#         diff = max - min
#         print(f'Difference between max and min values = {round(diff,3)}')
#         return diff
    
#     my_list = list_creation(n, limit)
#     print('List of real numbers:', my_list)
#     fractional_part_diff(my_list)