my_lambda = lambda x: x.lower()
my_lambda("HA HA HA")  # "ha ha ha"

square_lambda = lambda x: x ** 2
square_lambda(4)  # 16

equals_lambda = lambda x, y: x == y
equals_lambda(1, 2)  # False

print(my_lambda("HA HA HA"), square_lambda(4), equals_lambda(1, 2), sep=" * ")
#################################################
items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]
odds = list(filter(lambda x: x % 2, items))  # [1, 3, 5]

from functools import reduce

items_sum = reduce(lambda x, y: x + y, items)  # 15
#################################################
pairs = [(1, 10), (2, 9), (3, 8)]

sorted(pairs, key=lambda x: x[1])  # [(3, 8), (2, 9), (1, 10)]
min(pairs)  # (1, 10)
max(pairs, key=lambda x: x[1])  # (1, 10)
max(pairs, key=lambda x: x[0] * x[1])  # (3, 8)

