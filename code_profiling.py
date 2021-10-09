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