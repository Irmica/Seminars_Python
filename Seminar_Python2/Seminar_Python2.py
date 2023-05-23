n = int(input("Введите натуральное число: "))
f = 1
k = 2
while k<=n:
    f *= k
    k +=1
print(f"Факториал {n} равен {f}")
      