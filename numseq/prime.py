
def primes(n):
    """Returns a list of all prime numbers
    less than n"""

    noprimes = set(j for i in range(2, n) for j in range(i*2, n, i))
    primes = [x for x in range(2, n) if x not in noprimes]
    return primes


def is_prime(n):
    """Returns a boolean indicating whether n
    is a prime number"""
    from math import sqrt

    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True
