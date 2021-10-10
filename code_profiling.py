# -*- coding: utf-8 -*-

import timeit

if __name__ == "__main__":
    setup = "from math import sqrt"

    code = '''
data_ = [e for e in range(100)]
def func():
    return [sqrt(x) for x in data_ if x % 2 == 0]
'''

    code2 = '''
data_ = [e for e in range(100)]
def func():
    res = []
    for e in  data_:
        if e % 2 == 0:
            res.append(sqrt(e))    
    
    return res
'''

    print(timeit.timeit(stmt=code, setup=setup))
    print(timeit.timeit(stmt=code2, setup=setup))

#     setup2 = '''
# from __main__ import linear_search, binary_search
# import random
#     '''
#
#     linear_search_code = '''
# lst = sorted([random.randint(0, 1000000) for _ in range(1000)])
# to_find = random.randint(0, 1000000)
# result = linear_search(lst, to_find)
#     '''
#
#     binary_search_code = '''
# lst = sorted([random.randint(0, 1000000) for _ in range(1000)])
# to_find = random.randint(0, 1000000)
# result = binary_search(lst, to_find)
#     '''
#
#     print(timeit.timeit(stmt=linear_search_code, setup=setup2, number=1000))
#     print(timeit.timeit(stmt=binary_search_code, setup=setup2, number=1000))
