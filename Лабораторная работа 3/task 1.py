src = not False and True or False and not True

# TODO расписать упрощение выражения
# result = True and True or False and False # Избавляемся от отрицания ( упрощаем оператор not)
# result = True or False # избавляемся от "И" ( упрощаем оператор and)
# result = True # избавляемся от логического "или" ( упрощаем оператор or)
result = True  # TODO подставить результат выражения

print(src == result)
