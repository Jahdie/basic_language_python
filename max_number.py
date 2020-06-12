number = int(input("Введите положительное число: "))
while number < 0:
    number = int(input("Введите положительное число: "))
n = 0
m1 = 0
m2 = number
max = 0
while number > 0:
    n = number % 10
    if n == 9:
        max = n
        break
    if n > max:
        max = n
    m1 = number - n
    number = m1 / 10
    number = int(number)
print(f"Самая большая цифра в числе: {max}")
