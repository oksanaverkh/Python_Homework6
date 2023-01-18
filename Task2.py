# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

## Enumerate, lambda, filter, map were used
# New decision of the task: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os
os.system('cls')

def compression(string):
    compressed_string = ''
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        compressed_string += str(count) + string[i]
        i += 1
    return compressed_string

def decompression(string):
    num = ''
    decompressed_list = []
    for i, elem in enumerate(string):
        if elem.isdigit():
            num += elem
        else:
            decompressed_list.append(num)
            decompressed_list.append(elem)
            num=''
    num_list = list(filter(lambda s: int(s.isdigit()), decompressed_list))
    text_list = list(filter(lambda s: not s.isdigit(), decompressed_list))

    recovered_list = list(map(lambda x, y: int(x)*y, num_list, text_list))
    recovered_text = ''.join(recovered_list)
    return recovered_text

def main():
    text = input('Enter a text: ')
    print()
    print('Compressed text: ', compression(text))
    print('Recovered text: ', decompression(compression(text)))

if __name__ == '__main__':
    main()

# Previous decision

# def compression(string):
#     compressed_string = ''
#     i = 0
#     while i < len(string):
#         count = 1
#         while i + 1 < len(string) and string[i] == string[i + 1]:
#             count += 1
#             i += 1
#         compressed_string += str(count) + string[i]
#         i += 1
#     return compressed_string

# def decompression(string):
#     decompressed_string = ''
#     i = 0
#     while i < len(string)-1:
#         count = int(string[i])
#         decompressed_string += count*string[i+1]
#         i += 2
#     return decompressed_string

# def main():
#     text = input('Enter a text: ')
#     print()
#     print('Compressed text: ', compression(text))
#     print('Recovered text: ', decompression(compression(text)))
 
# if __name__ == '__main__':
#     main()