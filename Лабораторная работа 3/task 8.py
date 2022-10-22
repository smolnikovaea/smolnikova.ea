money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
loss = salary -(spend + (spend*(month*increase)))
ostalos = money_capital + loss
while ostalos >= 0:
    ostalos = money_capital = loss
    month += 1
    loss = salary -(spend + (spend*(month*increase)))
    money_capital += loss

print(month)


# TODO Оформить решение

#print(month)
