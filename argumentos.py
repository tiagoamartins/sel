def soma(a, b, *numeros):
    """
    Função que soma dois ou mais números.
    Objetivo é mostrar a utilização de um número não fixo de argumentos.
    O argumento 'numeros' é uma tupla que recebe do terceiro argumento
    em diante.
    O desempacotamento de tuplas/listas como argumentos também é possível
    e durante a expansão os dois primeiros argumentos serão colocados em
    'a' e 'b' e o resto em 'numeros'.

    >>> soma(1, 2)
    3
    >>> soma(1, 2, 3)
    6
    >>> soma(1, 2, 3, 4)
    10
    >>> numeros = [3, 4, 5]
    >>> soma(1, 2, *numeros)
    15
    >>> numeros = [1, 2, 3, 4, 5, 6]
    >>> soma(*numeros)
    21
    """

    soma = a + b
    for num in numeros:
        soma += num
    return soma


def foo(a, b, c, *args, **kwargs):
    """
    Função que imprime os diferentes argumentos e seus tipos.
    Demonstra a utilização de argumentos posicionais e nomeados, bem como
    o desempacotamento de tuplas/listas e dicionários.

    >>> foo(1, 2, 3, 4, 5, nome='Jose', idade=100, vivo=True)
    a: 1 <class 'int'>
    b: 2 <class 'int'>
    c: 3 <class 'int'>
    args: (4, 5) <class 'tuple'>
    kwargs: {'nome': 'Jose', 'idade': 100, 'vivo': True} <class 'dict'>
    >>> my_tuple = (2, 3)
    >>> my_dict = {'idade': 100, 'vivo': True}
    >>> foo(1, 4, 5, *my_tuple, nome='Jose', **my_dict)
    a: 1 <class 'int'>
    b: 4 <class 'int'>
    c: 5 <class 'int'>
    args: (2, 3) <class 'tuple'>
    kwargs: {'nome': 'Jose', 'idade': 100, 'vivo': True} <class 'dict'>
    """

    print('a: {} {}'.format(a, type(a)))
    print('b: {} {}'.format(b, type(b)))
    print('c: {} {}'.format(c, type(c)))
    print('args: {} {}'.format(args, type(args)))
    print('kwargs: {} {}'.format(kwargs, type(kwargs)))
