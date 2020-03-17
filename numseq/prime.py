# def new_way_prime(n):

#     not_prime_list = []
#     if n < 2:
#         return [2]
#     possible_list = [2]
#     possible_list.extend([x for x in range(3, n, 2) if x > 1])
#     print(possible_list)
#     mult = 1
#     for i in range(n):
#         mult += 1
#         sample = i * mult
#         if sample in possible_list:
#             possible_list.remove(sample)
#         not_prime_list.append(sample)
#     print(possible_list)


# new_way_prime(5)

# for possible_prime in range(3, n, 2):
#     if possible_prime in prime_dict:
#         return prime_dict
#     elif possible_prime in not_prime_dict:
#         return prime_dict
#     elif n % (n-1)


# def primes(n):
#     """Returns a list of all prime numbers
#     less than n"""

#     import math
#     if n < 2:
#         return []
#     elif n in primes_list:
#         return primes_list
#     else:
#         primes_list = [2]
#         for num in range(3, n, 2):
#             if all(num % i != 0 for i in range(3, int(math.sqrt(num))+1, 2)):
#                 primes_list.append(num)
#         return primes_list

# def primes(n):
#     import SymPy
#     return SymPy.primerange(1, n)

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
