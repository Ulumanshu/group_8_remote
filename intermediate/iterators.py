from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


class PrimeIterator:
    # Iterator that allows you to iterate over n primes
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


lst = get_n_primes(100)
for elem in lst:
    print(elem)

iter = PrimeIterator(100)
for elem in iter:
    print(elem)

list_iter = list(lst)[:5]
print(list_iter)

list_iter = list(lst)[:5]
print(list_iter)
#
# list_iter = iter[:5]
# print(list_iter)
