""" Задача 1.
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

# from sys import argv
# script_name, virabotka_v_chasah, stavka_v_chas, premia = argv
# salary = (int(vyrabotka_v_chasah) * int(stavka_v_chas)) + int(premia)
# print('Заработная плата: ', salary)

"""Задача 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
Результат: [12, 44, 4, 10, 78, 123]
"""

# my_list = [25, 30, 45, 50, 55, 60, 65, 70]
# print(f"Исходный список: {my_list}")
#
# new_list = [el for el in my_list if el % 2 == 0]
# print(f"Новый список: {new_list}")

"""Задача 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

# new_list = [el for el in range(20, 241) if el % 20 == 0] + [el for el in range(20, 241) if el % 21 == 0]
# print(new_list)

"""Задача 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
Результат: [23, 1, 3, 10, 4, 11]
"""

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = [el for el in my_list if my_list.count(el) < 2]
# print(new_list)

"""Задача 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce(). 
"""

# from functools import reduce
#
# my_list = [el for el in range(100, 1001) if el % 2 == 0]
#
# def my_func(prev_el, el):
#     return prev_el * el
#
# print(reduce(my_func, my_list[:]))

"""Задача 6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count
from itertools import cycle

# итератор, генерирующий целые числа, начиная с указанного:

# for el in count(3):
#     if el > 10:
#         break
#     else:
#         print(el)

# итератор, повторяющий элементы некоторого списка, определенного заранее:

# steps = ["one", "two", "three", "four"]
# i = 0
# for el in cycle(steps):
#     if i > 10:
#         break
#     print(el)
#     i += 1

"""Задача 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n)
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
"""

# def fact(n):
#     first_n = 1
#     for el in range(1, n+1):
#         first_n *= el
#         yield first_n
#
# n = int(input('Введите число: '))
#
# i = 1
# for el in fact(n):
#     print(f'Факториал числа {i}! = {el}')
#     i += 1
