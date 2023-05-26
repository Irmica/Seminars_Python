# 3.1[16]: Дан список целых чисел.  Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

# 	Примеры/Тесты:
#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
#     Output:  2

#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
#     Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# ```(*)``` **Усложнение.** При выводе результата на экран воспользуйтесь тернарным оператором.

# n = int(input("Введите число: "))
# list1 = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
# print((list1.count(n) if list1.count(n) !=0 else -1))

# -----------------------------------------------------------------------------------------
# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

# n = int(input("Введите число: "))
# list1 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# print(list1)
# min_difference = 10000000
# for item in list1:
#     if 0 <= (item - n) < min_difference:
#         min_difference = (item-n)
#         min_item = item
# print(min_difference, min_item)

# ---------------------------------------------------------------------------------------------
# #### 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

letters1 = {'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'}
letters2 = {'d', 'g'}
letters3 = {'b', 'c', 'm', 'p'}
letters4 = {'f', 'h', 'v', 'w', 'y'}
letters5 = {'k'}
letters8 = {'j', 'x'}
letters10 = {'q', 'z'}

english_1point = frozenset(letters1)
english_2point = frozenset(letters2)
english_3point = frozenset(letters3)
english_4point = frozenset(letters4)
english_5point = frozenset(letters5)
english_8point = frozenset(letters8)
english_10point = frozenset(letters10)

english_point = {english_1point: 1, english_2point: 2, english_3point: 3,
                 english_4point: 4, english_5point: 5, english_8point: 8, english_10point: 10}

word = (input("Введите слово на английском языке для подсчета очков: ")).lower()
points = 0
for item in word:
    for key in english_point:
        if item in key:
            points += english_point[key]
print(f"Количество очков за слово {word} равно {points}")
