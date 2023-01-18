# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


## List comprehension, enumerate, lambda were used
# New decision of the task: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
import random
from functools import reduce
os.system('cls')

def check():
    num = int(input())
    while not num >=1:
        print('Wrong number, try again')
        num = int(input())
    return int(num)

def sum_find(new_list):
        sum_odd_indexes_values = 0
        odd_list = [elem for i, elem in enumerate(new_list) if i%2!=0]
        sum_odd_indexes_values = reduce((lambda x, y: x+y), odd_list)
        return sum_odd_indexes_values

def main():
    print('Enter list length: ', end='')
    n = check()
    print('Enter list limit value: ', end='')
    limit = check()
    my_list = [random.randint(-limit, limit) for _ in range(n)]
    print(my_list)
    print('Sum of elements with odd indexes = ', sum_find(my_list))

if __name__ == '__main__':
    main()


# Previous decision
# import os
# import random
# os.system('cls')

# n = int(input('Enter list length: '))
# limit = int(input('Enter list limit value: '))

# if n <= 0 or limit <= 0:
#     print('Enter another value')

# else:
#     def list_creation(n, limit):
#         new_list = []
#         for _ in range(n):
#             new_list.append(random.randint(-limit, limit))
#         return new_list

#     def sum_find(new_list):
#         sum_odd_indexes_values = 0
#         for i in range(len(new_list)):
#             if i % 2 != 0:
#                 sum_odd_indexes_values += new_list[i]
#         return sum_odd_indexes_values

#     my_list = list_creation(n, limit)

#     print(my_list)
#     print('Sum of elements with odd indexes = ', sum_find(my_list))