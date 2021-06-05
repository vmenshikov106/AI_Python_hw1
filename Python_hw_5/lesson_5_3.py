"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

salarys = []

with open('salary.txt', encoding='utf-8') as my_f:
    lines = my_f.readlines()
    for line in lines:
        name, salary = line.split(" ")
        salary = int(salary)
        salarys.append(salary)
        if salary < 20000:
            print('Оклад менее 20 000 у сотрудников: ', name)
            
    print("Средний доход сотрудников: ", round(sum(salarys) / len(salarys), 2))

