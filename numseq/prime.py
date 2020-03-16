def primes(n):
    """Returns a list of all prime numbers
    less than n"""

    import math
    if n < 2:
        return []
    else:
        primes_list = [2]
        for num in range(3, n, 2):
            if all(num % i != 0 for i in range(3, int(math.sqrt(num))+1, 2)):
                primes_list.append(num)
        return primes_list


def is_prime(n):
    """Returns a boolean indicating whether n
    is a prime number"""

    primes_list = primes(n+1)
    print(primes_list)
    return n in primes_list
