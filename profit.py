revenue = int(input("Введите сумму выручки: "))
costs = int(input("Введите сумму издержек: "))
profit = revenue - costs
if profit > 0:
    profitability = (profit / revenue) * 100
    print(f"Ваша прибыль: {profit} руб.")
    print(f"Ваша рентабельность: {profitability:.1f}%")
elif profit == 0:
    print(f"Ваша прибыль покрыла издержки.")
else:
    print(f"Ваш убыток: {profit * -1} руб.")
if profit > 0:
    employee = int(input("Введите количесто сотрудников фирмы: "))
    profit_employee = profit / employee
    print(f"Прибыль фирмы в расчёте на одного сотрудника составляет: {profit_employee:.1f} руб.")
