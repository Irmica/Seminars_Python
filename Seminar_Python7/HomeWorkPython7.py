# #### 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.

# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# 	Примеры/Тесты:
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# **Примечание.**

# - Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# - Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно некоторые проверки не нужны.

# ```(*)``` **Усложнение.**

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о кол-ве гласных букв в фразах. Эта информация возвращается в виде списка словарей. Каждый элемент списка(словарь) соответствует фразе.

# 	Примеры/Тесты:
# 		<function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

# def rhythm(poem: str, c=True):
#     phrases = poem.split(" ")
#     vowels = 'уеыаоэяию'
#     list_of_vowels = []
#     if c == True:
#         for idx in range(len(phrases)):
#             list_of_vowels.append(
#                 [letter for letter in phrases[idx] if letter.lower() in vowels])

#         number_of_vowels = []
#         for item in list_of_vowels:
#             set_vowels = set(item)
#             list_count = []
#             for idx3 in set_vowels:
#                 list_count.append(item.count(idx3))
#             number_of_vowels.append(dict(zip(set_vowels, list_count)))
#         for idx2 in range(len(list_of_vowels)):
#             if len(list_of_vowels[idx2]) != len(list_of_vowels[idx2-1]):
#                 return (f"False, {number_of_vowels}")
#         return (f"True, {number_of_vowels}")
#     else:
#         for idx in range(len(phrases)):
#             list_of_vowels.append(
#                 [letter for letter in phrases[idx] if letter.lower() in vowels])
#         for idx2 in range(len(list_of_vowels)):
#             if len(list_of_vowels[idx2]) != len(list_of_vowels[idx2-1]):
#                 return False
#         return True


# print(rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", False))
# print(rhythm("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
# print(rhythm("пара-ра-рам рам-пум-пупам па-ре-по-дам"))
# print(rhythm("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
# print(rhythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
# print(rhythm("Пам-парам-пурум Пум-пурум-карам"))
#-------------------------------------------------------------------------------------------------------------------

# #### 6.2[32]: Напишите функцию ```print_operation_table(operation, num_rows=6, num_columns=6)```, которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы ```num_rows``` и ```num_columns``` указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.

# 	Примеры/Тесты:
#     print_operation_table(lambda x,y: x**y,4,4)
# 	1   1   1   1
# 	2   4   8  16
# 	3   9  27  81
# 	4  16  64 256

#     print_operation_table(lambda x,y: x*y)
# 	1   2   3   4   5   6
# 	2   4   6   8  10  12
# 	3   6   9  12  15  18
# 	4   8  12  16  20  24
# 	5  10  15  20  25  30
# 	6  12  18  24  30  36

# ```(*)``` **Усложнение.** Сформируйте форматированный вывод с номерами строк и столбцов

# 	Примеры/Тесты:
# 	print_operation_table(lambda x,y: x**y,4,4)
# 	       1   2   3   4
# 	    ----------------
# 	1 |    1   1   1   1
# 	2 |    2   4   8  16
# 	3 |    3   9  27  81
# 	4 |    4  16  64 256

# 	print_operation_table(lambda x,y: x*y)
# 	       1   2   3   4   5   6
# 	    ------------------------
# 	1 |    1   2   3   4   5   6
# 	2 |    2   4   6   8  10  12
# 	3 |    3   6   9  12  15  18
# 	4 |    4   8  12  16  20  24
# 	5 |    5  10  15  20  25  30
# 	6 |    6  12  18  24  30  36

def print_operation_table(func, num_rows, num_columns):
    first_string = '       '
    for number in range(1, num_columns+1):
        first_string += str(number).rjust(3) + ' '
    print(first_string)
    print('      '+'-'*(4*num_columns), end="\n")
    # for idx_rows in range(1, num_rows+1):
    #     print(f"{(str(idx_rows)).rjust(3)} | ", end="")
    #     for idx_columns in range(1, num_columns+1):
    #         print((str(func(idx_rows, idx_columns))).rjust(3), end=" ")
    #     print('\n')
    for idx_rows in range(1, num_rows+1):
        begin_string = (f"{(str(idx_rows)).rjust(4)} |")
        for idx_columns in range(1, num_columns+1):
            begin_string += ((str(func(idx_rows, idx_columns))).rjust(4))
        print(begin_string)
    print('\n')
    


print_operation_table(lambda x, y: x**y, 4, 4)
print_operation_table(lambda x, y: x*y, 6, 6)