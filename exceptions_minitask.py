from string import digits, ascii_letters, ascii_uppercase, ascii_lowercase

# 1. Sugeneruoti nauja lista kur butu einamas narys padelintas is sekancio nario, * passktinis is pirmo
# * Naudokite for cikla su su try except
# 2. Susumuoti naujo listo narius.

data_array = [1, '666', 56, 48, '66.78', '9,5', 10, 0.99, 0, '0,0', 'k5', '123', '52,54k8']
data_array_2 = list()


def safe_convert(value):
    delimeter_list = ['.', ',']
    res = 0
    try:
        res = float(value)
    except Exception as err:
        if type(value) == str:
            transform_elem = [
                letter for letter in value if letter in digits or letter in delimeter_list
            ]  # paima is k5 tik skaiciu 5
            new_value = ''.join(transform_elem)
            res = float(new_value.replace(',', '.'))
            print(err)

    return res


for nr, elem in enumerate(data_array):
    print(nr, elem)
    try:
        tr_elem = safe_convert(elem)
        next_elem = safe_convert(data_array[nr + 1])

    except IndexError as err:
        print("Index: ", err)
        tr_elem = safe_convert(elem)
        next_elem = safe_convert(data_array[0])

    try:
        result = tr_elem / next_elem
        data_array_2.append(result)

    except ZeroDivisionError as err:
        result = tr_elem / 1
        print("Division: ", err)
        data_array_2.append(result)

    except Exception as err:
        print("SKIPPING", err, nr, )
        continue

print(data_array_2)
print(sum(data_array_2))


# print(digits)
#
# for nr, elem in enumerate(data_array):
#     print(nr, elem)
#     try:
#         elem = float(elem)
#     except ValueError:
#         print(ValueError)
#         transport_elem = [leter for leter in elem if leter in digits or leter in ['.', ',']]       # paima is k5 tik skaiciu 5
#         new_elem = ''.join(transport_elem)
#         elem = float(new_elem.replace(',', '.'))
#
#     try:
#         next_elem = float(data_array[nr+1])
#         print("I AM NEXT FOR: ", elem, next_elem, type(next_elem))
#     except ValueError:
#         # print(next_elem)
#         # print(type(next_elem))
#         if type(next_elem) == str:
#             transport_elem_2 = [leter for leter in next_elem if leter in digits or leter in ['.', ',']]
#             next_elem = ''.join(transport_elem_2)
#             next_elem = float(next_elem.replace(',', '.'))
#         else:
#             next_elem = next_elem
#
#     except IndexError as err:
#         print("Index:", err)
#         next_elem = float(data_array[0])
#
#     try:
#         result = elem / next_elem
#         data_array_2.append(result)
#
#     except ZeroDivisionError as err:
#         result = elem / 1
#         print(err)
#         data_array_2.append(result)
#
#     except Exception as err:
#         print(err)
#         continue
#
#
# print(data_array)
# print(data_array_2)