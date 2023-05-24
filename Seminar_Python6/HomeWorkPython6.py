# # Практическое задание 6. «Повторение списков»
# *Обновлено xx.xx.xxxx*

# Усложнение задач выделены ```(*)```. Они необязательны для решения и нужны для тех, кому мало выполнить обычное задание.
# Если вы хотите решить усложненное задание - сначала сделайте задание обычной сложности.

# #### 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :

# - Первый элемент прогрессии, Разность (шаг) и Количество элементов

# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# 	Напишите функцию
	
# 	- Аргументы: три указанных параметра
# 	- Возвращает: список элементов арифмитической прогрессии.

# 	Примеры/Тесты:
   
# 	Ввод: 7 2 5
# 	Вывод: [7 9 11 13 15]
# 	Ввод: 2 3 12
# 	Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# ```(*)``` **Усложнение.** Для формирования списка внутри функции используйте Comprehension


# ```(**)``` **Усложнение.** Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, вам понадобится распаковка и Comprehension или map
	


# #### 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# 	Напишите функцию
#     - Аргументы: список чисел и границы диапазона
#     - Возвращает: список индексов элементов (смотри условие)

# 	Примеры/Тесты:
#     lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#     <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
#     <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
#     <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

# ```(*)``` **Усложнение.**  Для формирования списка внутри функции используйте Comprehension

# ```(*)``` **Усложнение.**  Функция возвращает список кортежей вида: индекс, значение

# 	Примеры/Тесты:
#     lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#     <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]


