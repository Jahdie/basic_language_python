seconds_enter = int(input("Введите количество секунд:"))
hours = seconds_enter // 3600
minuts = (seconds_enter // 60) % 60
seconds = seconds_enter % 60
if hours < 10:
    h = '0' + str(hours)
else:
    hours = str(hours)
if minuts < 10:
    minuts = '0' + str(minuts)
else:
    m = str(minuts)
if seconds < 10:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)
print(f"{hours}:{minuts}:{seconds}")
