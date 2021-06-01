"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""


with open("file_4.txt", "w") as my_f:
    num = f"{input('Введите числа через пробел: ')}"
    my_f.write(num)

with open("file_4.txt", "r") as my_f:
    main_line = my_f.readline()
    main_list = map(int, main_line.split())
    print("Сумма введённых чисел: ", sum(main_list))
    
    
