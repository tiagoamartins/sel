""" Módulo de números da sequência de Fibonacci """


def fib(n):   # return Fibonacci series up to n
    """
    Retorna uma lista contendo os números da sequência de Fibonacci até n

    >>> fib(10)
    [1, 1, 2, 3, 5, 8]
    >>> fib(-1)
    []
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
