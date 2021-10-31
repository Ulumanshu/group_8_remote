from functools import reduce


def lowercase_normal(text_):
    return text_.lower()

lowercase_lambda = lambda text_: text_.lower()

print(lowercase_normal("HA HA HA"))  # "ha ha ha"
print(lowercase_lambda("HA HA HA"))  # "ha ha ha"

items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]
odds = list(filter(lambda x: x % 2, items))  # [1, 3, 5]

print(type(filter(lambda x: x % 2, items)))
print(filter(lambda x: x % 2, items))
for val_ in filter(lambda x: x % 2, items):
    print(val_)
odds_filter_comprehension = [od for od in items if od % 2]

items_sum = reduce(lambda x, y: x + y, items)  # 15

print(squared)
print(odds)
print(odds_filter_comprehension)

print(items_sum)
