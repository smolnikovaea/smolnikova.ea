list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index  = 0
for i in range(len(list_numbersber)):
    max_number = list_numbers[max_index]
    current_number = list_numbers[i]
    if current_number > list_numbers[max_index]:
        max_index = i


        last_index = list_numbers[-1]
        list_numbers[-1] = list_numbers[max_index]
        list_numbers[max_index] = last_index

print(list_numbers)
