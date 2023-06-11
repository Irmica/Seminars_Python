# from os.path import join, abspath, relpath, dirname, exists

# main_dir = join(".")
# filename = join(main_dir, "data", "data1.txt")
# print(filename)
# print(exists(filename))

# file = open(filename, mode="rt", encoding="utf-8")
# for line in file:
#     print(line.strip())
# file.close()

# with open(filename, mode="rt", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())


# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием
# os.path и pathlib
# import os
# import os.path as path1

# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# #print(os.getcwd())
# print(MAIN_DIR)
# file_name = path1.join(MAIN_DIR, "data", "data2.csv")
# with open(file_name, mode="r", encoding="utf-8") as file:
#     persons = []
#     for line in file:
#        # print(*(line.strip().split("#")))
       
#         last_name, first_name, parent = line.strip().split("#")
#         family = [last_name, first_name, parent]
#         persons.append(family)
#         print(last_name, first_name, parent)
#     print(persons)


# №7.2[###]. Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И
# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым?
# import os
# import os.path as path1

# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# #print(os.getcwd())
# print(MAIN_DIR)
# file_name = path1.join(MAIN_DIR, "data", "data2.csv")
# with open(file_name, mode="r", encoding="utf-8") as file:
#     persons = []
#     for line in file:
#        # print(*(line.strip().split("#")))
       
#         last_name, first_name, parent = line.strip().split("#")
#         family = [last_name, first_name, parent]
#         persons.append(family)
        

#     # print(item[0]+' '+ item[1][0] + '.' + item[2][0] + '.')
#     # print(item[0]+'-'+ item[1][0] + '-' + item[2][0])
#     # print(f"{item[0]} {item[1][0]}.{item[2][0]}.")
    
# file_names = path1.join(MAIN_DIR, "names.txt")   
# with open(file_names, mode="wt", encoding="utf=8") as file_write:
#     for last_name, first_name, parent in persons:
#         file_write.write((f"{last_name} {first_name[0]}.{parent[0]}.\n"))


# №7.3[###]. Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# преобразовать его в списки вида
# 1) ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]
# 2) ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]
# с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
# [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы, в которых первая буква П



# №7.4[49]. Напишите функцию same_by(func, objects)
# которая проверяет, все ли элементы в objects дают одинаковое значение характеристики func
# Аргументы:
# func - функция одного аргумента.
# objects - список или кортеж
# Возвращаемое значение:
# - Если objects пустой, вернуть None
# - Если все элементы в objects дают одинаковое значение func, вернуть True, иначе вернуть False
# # Примеры/Тесты:
# same_by(lambda x: x % 2, [1, 2, 10, 12]) -> False
# same_by(lambda x: x % 2, [0, 2, 10, 12]) -> True
# same_by(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]) -> True
# same_by(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
# same_by(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]) -> False
# same_by(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> True
# same_by(lambda x: x[0], ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]) -> False
# same_by(lambda x: x[0], ["qz", "qr1", "qz", "qi", "qz", "qs", "qz", "qh"]) -> True
# [*] Усложнение. Не используйте цикл в функции

def same_by(func, objects):
    if len(objects) == 0 : return None
    for idx in range(1, len(objects)):
        if func(objects[idx]) != func(objects[idx-1]): return False
        return True
    
print(same_by(len, ["qw", "er", "ty", "ui", "op", "as", "df", "gh"]))
print(same_by(len, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]))
print(same_by(max, ["qw", "er1", "ty", "ui", "op", "as", "df", "gh"]))
print(same_by(max, ["qz", "zr1", "tz", "zi", "oz", "zs", "dz", "zh"]))