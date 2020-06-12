a = int(input("Введите a км.: "))
b = int(input("Введите b км.: "))
while a < 0 or b < 0:
    a = int(input("Введите a км.: "))
    b = int(input("Введите b км.: "))
result = a
day = 1
print(f"\nРезультат:\n{day}-й день: {a} км.")
while b > result:
    day += 1
    result = result * 0.10 + result
    print(f"{day}-й день: {result:.2f} км.")
print(f"\nОтвет: на {day}-й день спортсмен достиг результата — не менее {b} км.")
