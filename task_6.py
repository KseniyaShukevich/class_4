from itertools import count, cycle


def generate_numbers(n):
    for el in count(n):
        if el > 10:
            break

        print(el)


generate_numbers(2)


def repeat_list(my_list):
    counts = 0

    for el in cycle(my_list):
        counts += 1
        if counts > 15:
            break

        print(el)


repeat_list([1, 3, 5, 7])
