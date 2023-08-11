
# from random import randint
# array = int(input('Введите колличество элементов массива:  '))
# start_list =[]
# end_list =[]


# min_index = int(input('Введите минимальный индекс:  '))
# max_index = int(input('Введите максимальный индекс:  '))

# if max_index<min_index or max_index>array or min_index>array:
#     print()
#     print('EROR: некорректный ввод данных')
#     quit()
# full = []
# for i in range(max_index+1):
#     if i>= min_index and i<= max_index:
#         full.append(i)
#         for a in range(array+1):
#             start_list.append(randint(1,100))
#             if a == i:
#                 end_list.append(start_list[a])


# if start_list==full==end_list:
#     start_list.append(1)
#     full.append(0)
#     end_list.append(1)


# print(f'все элементы {start_list}')
# print()
# print(f'индексы {full}')
# print(f'элементы {end_list}')

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint

array = int(input('Введите колличество элементов:  '))
min_element = int(input('Введите минимальный элемент:  '))
max_element = int(input('Введите максимальный элемент:  '))
start_list = []
for i in range(array):
    start_list.append(randint(1,100))
    element_list = [ i for i in start_list if i>=min_element and i<max_element+1 or i<=max_element and i>min_element-1]
    index_list=[i for i in range(len(start_list)) if min_element<= start_list[i]<=max_element]


print(f'все элементы {start_list}')
print()
print(f'индексы {index_list}')
print(f'элементы {element_list}')
