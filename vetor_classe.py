"""
>>> from random import randint
>>> lista_vetores = [Vetor(x=randint(-10, 10), y=randint(-10, 10)) for _ in range(5)]
>>> for x, y in lista_vetores:
...     print(x, y)
"""
import math
from numbers import Real


class Vetor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vetor({x}, {y})".format(x=self.x, y=self.y)

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __sub__(self, outro):
        return Vetor(self.x - outro.x, self.y - outro.y)

    def __mul__(self, valor):
        if isinstance(valor, Real):
            return Vetor(self.x * valor, self.y * valor)
        return NotImplemented

    def __rmul__(self, valor):
        return self * valor

    def __pos__(self):
        return self

    def __neg__(self):
        return self * -1

    def __iter__(self):
        yield self.x
        yield self.y


class VetorMutavel(Vetor):
    def __iadd__(self, outro):
        if isinstance(outro, Vetor):
            self.x += outro.x
            self.y += outro.y
            return self
        return NotImplemented

    def __imul__(self, outro):
        if isinstance(outro, Real):
            self.x *= outro
            self.y *= outro
            return self
        return NotImplemented
