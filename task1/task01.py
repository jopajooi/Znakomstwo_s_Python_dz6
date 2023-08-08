# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

one_element = int(input('Введите первый элемент:  '))
difference_element =int(input('Введите разность элементов:  '))
in_total_element =int(input('Введите колличество элементов:  '))
full_element = [in_total_element]

for i in range(in_total_element):
    print(one_element + i * difference_element)