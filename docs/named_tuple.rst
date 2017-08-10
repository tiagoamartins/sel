Utilizando ``namedtuple``
=========================

.. testcode::

        from collections import namedtuple

        Vetor = namedtuple('Vetor', ['x', 'y'])

.. doctest::

        >>> v = Vetor(x=10, y=5)
        >>> v.x == v[0] == 10
        True
        >>> v.y == v[1] == 5
        True

Retorna um vetor que representa a soma dos vetores v1 e v2 (v1 + v2)

.. testcode::

        def soma_vetor(v1, v2):
            return Vetor(x=v1.x + v2.x, y=v1.y + v2.y)

.. doctest::

        >>> v1 = Vetor(5, 2)
        >>> v2 = Vetor(2, 7)
        >>> soma_vetor(v1, v2)
        Vetor(x=7, y=9)

Retorna um vetor que representa a soma dos vetores v1 e v2 (v1 + v2)

.. testcode::

        def subtrai_vetor(v1, v2):
            return Vetor(x=v1.x - v2.x, y=v1.y - v2.y)

.. doctest::

        >>> v1 = Vetor(3, 4)
        >>> v2 = Vetor(1, 5)
        >>> subtrai_vetor(v1, v2)
        Vetor(x=2, y=-1)
