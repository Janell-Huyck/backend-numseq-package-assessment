mydict = {}


def fib(n):
    """Returns the nth number in the
    Fibonacci sequence"""

    if n in mydict:
        return mydict[n]
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        mydict[n] = result
        return result
