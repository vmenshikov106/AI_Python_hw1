
"""Поработать с переменными, создать несколько, вывести на экран, запросить у пользователя несколько чисел и строк и сохранить в переменные, вывести на экран.
"""

age = input('Введите Ваш возраст: ')
print('Ваш возраст:', age, 'лет (:')
name = input('Как вас зовут?')
print('Итого, получается...')
print('Вас зовут ', name, 'и Вам', age, 'лет!')

"""Пользователь вводит время в секундах. Перевести время в часы, минуты и секунды и выведите в формате чч:мм:сс. Использовать форматирование строк.
"""

time = int(input('Введите время в секундах: '))
seconds = time
minutes = seconds // 60
hours = minutes // 60
print("Введённое время в секундах в часах = ")
print("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))

"""Узнайть у пользователя число n. Найти сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

sum = input('Введите какое-нибудь число: ')
sum1 = int(sum)
sum2 = int(sum + sum)
sum3 = int(sum + sum + sum)
sum_result = sum1 + sum2 + sum3
print(sum_result)

"""Пользователь вводит целое положительное число. Найти самую большую цифру в числе. Для решения использовать цикл while и арифметические операции.
"""

num = int(input('Введите целое положительное число: '))
max = num%10
num = num//10
while num > 0:
    if num%10 > max:
        max = num%10
    num = num//10
print('Наибольшая цифра в введённом числе: ', max)

"""Запросить у пользователя значения выручки и издержек фирмы. Определить, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Вывести соответствующее сообщение.
Если фирма отработала с прибылью, вычислить рентабельность выручки (соотношение прибыли к выручке).
Далее запросить численность сотрудников фирмы и определить прибыль фирмы в расчете на одного сотрудника.
"""

proceeds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
profit = proceeds - costs
if proceeds > costs:
    profitability = profit/proceeds
    print('Фирма работает с прибылью, выручка больше издержек')
    print('Рентабельность фирмы - ', (profit / proceeds))
    employees = int(input('Какое количество сотрудников в вашей фирме? '))
    print('Прибыль фирмы в расчёте на одного сотрудника составляет: ', (profit/employees))
else:
    print('Фирма работает в убыток :((')

"""Задание 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.

Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

start_a = 2
finish_b = 3
day = 1
print('Результат:')
print(f'{day}-й день:', start_a)
while start_a <= finish_b:
    upper = start_a * 0.1
    start_a = start_a + upper
    day = day + 1
    print(f'{day}-й день: {start_a:.2f}')

print(f'На {day}-й день день спортсмен достиг результата — не менее 3 км')
