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


gen = prime_generator(10)
print(type(gen))
for elem in gen:
    a = input("Continue: ")
    print(elem)