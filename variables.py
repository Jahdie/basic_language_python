name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
day_birth = int(input("Введите день вашего рождения: "))
month_birth = int(input("Введите месяц вашего рождения числом: "))
year_birth = int(input("Введите год вашего рождения: "))
sex = input("Введите свой пол (М или Ж): ")
while True:
    if sex == "М" or sex == "Ж":
        break
    else:
        sex = input("Введите свой пол (М или Ж): ")
if month_birth == 1:
    month_birth = "января"
elif month_birth == 2:
    month_birth = "февраля"
elif month_birth == 3:
    month_birth = "марта"
elif month_birth == 4:
    month_birth = "апреля"
elif month_birth == 5:
    month_birth = "мая"
elif month_birth == 6:
    month_birth = "июня"
elif month_birth == 7:
    month_birth = "июля"
elif month_birth == 8:
    month_birth = "августа"
elif month_birth == 9:
    month_birth = "сентября"
elif month_birth == 10:
    month_birth = "октября"
elif month_birth == 11:
    month_birth = "ноября"
elif month_birth == 12:
    month_birth = "декабря"
print(f"\nЗдравствуйте, {name} {surname}! Ваша дата рождения: {day_birth} {month_birth} {year_birth} года.")
if sex == "М" and 2020 - year_birth < 30:
    print(f"Вы еще молоды и до пенсии вам {65 - (2020 - year_birth)} лет")
elif sex == "М" and 2020 - year_birth > 30:
    print(f"Вы уже не так молоды и пора думать о пенсии, которая наступит через {65 - (2020 - year_birth)} лет")
elif sex == "Ж" and 2020 - year_birth < 30:
    print(f"Вы еще молоды и до пенсии вам {60 - (2020 - year_birth)} лет")
elif sex == "Ж" and 2020 - year_birth > 30:
    print(f"Вы уже не так молоды и пора думать о пенсии, которая наступит через {60 - (2020 - year_birth)} лет")
