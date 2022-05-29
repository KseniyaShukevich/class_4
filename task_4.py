my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_numbers = set()
repeated_numbers = set()

for number in my_list:
    if number in unique_numbers:
        unique_numbers.remove(number)
        repeated_numbers.add(number)
        continue

    if number not in unique_numbers and number not in repeated_numbers:
        unique_numbers.add(number)

print([el for el in my_list if el in unique_numbers])
