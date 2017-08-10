"""
Oferece um vetor matemático e operações de vetor

>>> v = Vetor(x=10, y=5)
>>> v.x == v[0] == 10
True
>>> v.y == v[1] == 5
True
"""

from collections import namedtuple


Vetor = namedtuple('Vetor', ['x', 'y'])


def soma_vetor(v1, v2):
    """
    Retorna um vetor que representa a soma dos vetores v1 e v2 (v1 + v2)

    >>> v1 = Vetor(5, 2)
    >>> v2 = Vetor(2, 7)
    >>> soma_vetor(v1, v2)
    Vetor(x=7, y=9)
    """
    return Vetor(x=v1.x + v2.x, y=v1.y + v2.y)


def subtrai_vetor(v1, v2):
    """
    Retorna um vetor que representa a soma dos vetores v1 e v2 (v1 + v2)

    >>> v1 = Vetor(3, 4)
    >>> v2 = Vetor(1, 5)
    >>> subtrai_vetor(v1, v2)
    Vetor(x=2, y=-1)
    """
    return Vetor(x=v1.x - v2.x, y=v1.y - v2.y)
