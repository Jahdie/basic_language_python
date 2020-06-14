n = int(input("Введите номер месяца: "))
seasons_list = [
    "январь", "февраль", "март",
    "апрель", "май", "июнь",
    "июль", "август", "сентябрь",
    "октябрь", "ноябрь", "декабрь"
]
seasons_dict = {
    "зима": ["декабрь", "январь", "февраль"],
    "весна": ["март", "апрель", "май"],
    "лето": ["июнь", "июль", "август"],
    "осень": ["сентябрь", "октябрь", "ноябрь"]
}
month = seasons_list[n - 1]
for season in seasons_dict.items():
    if month in season[1]:
        print(f"{month.title()} это {season[0]}.")
