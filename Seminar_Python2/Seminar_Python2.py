# n = int(input("Введите натуральное число: "))
# f = 1
# k = 2
# while k<=n:
#     f *= k
#     k +=1
# print(f"Факториал {n} равен {f}")
      
# n = int(input("Введите натуральное цисло: "))
# f1 = 0
# f2 = 1
# f3 = 0
# i = 2
# while f3 < n:
#     f3 = f1+f2
#     f1 = f2
#     f2 = f3
#     i += 1
#     if f3 > n:
#         i = 0
# if i == 0:
#     print(-1)
# else:
#     print(f"Число {n} является {i} в ряду Фибоначчи")

# n = int(input("Введите количество дней: "))
# count = 0
# max = 0
# for i in range(1, n+1):
#     x = int(input(f"Введите среднесуточную температуру для дня {i}: "))
#     if x > 0:
#         count +=1
#     else: count = 0
#     if  max < count:
#         max = count
# print(f"Максимальная длительность оттепели {max} дней.")  

n = int(input("Введите количество арбузов: "))
max = 0
min = 1001
for i in range(n):
    m = int(input("Введите массу арбуза: "))
    if max < m:
        max = m
    if min > m:
        min = m
print(f"Для тещи арбуз массой {min} кг, для себя арбуз {max} кг.")