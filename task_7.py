from functools import reduce


def get_factorials(n):
    for number in range(1, n + 1):
        yield reduce(lambda a, b: a * b, [el + 1 for el in range(number)])


for factorial in get_factorials(6):
    print(factorial)
