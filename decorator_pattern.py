import functools

data_dict = {}

def cache(fn):
    _cache = dict()

    @functools.wraps(fn)
    def cacher(*args):
        if args not in _cache:
            _cache[args] = fn(*args)
        # print(_cache, args)

        return _cache[args]

    global data_dict
    data_dict = _cache

    return cacher


@cache
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


result = fibonacci(35)
print(data_dict)
print(result)
