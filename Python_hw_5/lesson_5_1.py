"""1) Cоздать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


my_f = open("file.txt", "x")
str_list = ('\n'.join(list(input("Введите какие-нибудь данные: ").split())))
my_f.writelines(str_list)
my_f.close()

