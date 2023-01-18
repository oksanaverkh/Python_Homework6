# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# List comprehesion, zip, filter, map, lambda were used
# New decision of the task: Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
import random
os.system('cls')

def check():
    k = int(input('Enter degree K: '))
    while not 0<=k<=100:
        print('Wrong value, try again')
        k = int(input('Enter degree K: '))
    return int(k)

def main():
    k = check()    
    coef_list = [random.randint(0,100) for i in range(k+1)]
    variables_list = ['x^'+str(k-i) for i in range(k)] + ['']

    polynomial_list = [str(i)+j for i,j in zip(coef_list,variables_list)]
    polynomial_list = [i.replace('x^1', 'x') for i in polynomial_list]
    polynomial_list = list(filter(lambda x: not x.startswith('0x'), polynomial_list))
    polynomial_list = list(map(lambda x: x.replace('1x', 'x') if x.startswith('1x') else x, polynomial_list))

    polynomial = ' + '.join(polynomial_list)+' = 0'

    print(coef_list)
    print()
    print(polynomial)

    with open('polynomial.txt', 'w') as data:
        data.write(polynomial)

if __name__ == "__main__":
    main()

# # Previous decision
# import os
# import random
# os.system('cls')

# def list_creation(num, limit):
#     new_list = []
#     for _ in range(num+1):
#         new_list.append(random.randint(0, 100))
#     print('List of coefficients:', new_list)
#     return new_list

# def check():
#     k = int(input('Enter degree K: '))
#     while not 0<=k<=100:
#         print('Wrong value, try again')
#         k = int(input('Enter degree K: '))
#     return int(k)

# def main():
#     k = check()    
#     coef_list = list_creation(k, 100)
#     with open('polynomial.txt', 'w') as data:
#         for i in range(k+1):
#             if coef_list[i]==0:
#                 continue
#             elif coef_list[i]==1:
#                 data.write(f' x^{k-i} +')
#             elif (k-i)==1:
#                 data.write(f' {coef_list[i]*1}x +')
#             elif (k-i)==0:
#                 data.write(f' {coef_list[i]*1}')
#             else:
#                 data.write(f' {coef_list[i]}x^{k-i} +')
#         data.write(' = 0')

# if __name__ == "__main__":
#     main()