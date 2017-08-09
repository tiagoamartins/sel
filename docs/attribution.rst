Atribuições Múltiplas
=====================

Em Python é possível fazer múltiplas atribuições através da utilização de
tuplas:

.. doctest::

        >>> a = 10
        >>> b = 20
        >>> print(a)
        10
        >>> print(b)
        20

        >>> a, b = 40, 50
        >>> print(a)
        40
        >>> print(b)
        50


Fibonacci
---------

Exemplo de uma função que exibe na tela a sequência de Fibonacci até n:

.. testcode::

        def fib_print(n):
            a, b = 0, 1
            while b < n:
                print(b, end=' ')
                a, b = b, a+b
            print()

.. doctest::

        >>> fib_print(10)  # doctest: +NORMALIZE_WHITESPACE
        1 1 2 3 5 8
        >>> fib_print(-1)
        <BLANKLINE>

Exemplo que retorna uma lista contendo os números da sequência de Fibonacci até
n:

.. testcode::

        def fib(n):   # return Fibonacci series up to n
            result = []
            a, b = 0, 1
            while b < n:
                result.append(b)
                a, b = b, a+b
            return result

.. doctest::

        >>> fib(10)
        [1, 1, 2, 3, 5, 8]
        >>> fib(-1)
        []
