from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator(n):
    # Generator for iterating over n primes
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            print("Yield Happens!!!")
            yield number

            generated_numbers += 1
        number += 1


def prime_former(n):
    # form list of primes
    res = []
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            print("Look in Former Happens!!!")
            res.append(number)

            generated_numbers += 1
        number += 1

    return res


gen = prime_generator(10)
print(type(gen))
for elem in gen:
    a = input("Continue: ")
    print(elem)

formed = prime_former(10)
for elem_f in formed:
    a = input("Continue: ")
    print(elem_f)
