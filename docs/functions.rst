Funções
=======

Esse módulo demonstra a criação e utilização de funções, bem como a utilização
de valores padrão nos argumentos, permitindo que o argumento assuma um valor
quando não passado na chamada da função.

Argumentos opcionais
--------------------

A utilização de argumentos opcionais  com valores padrão e a passagem de
argumentos de forma posicional e nomeada.

.. testcode::

        def dolar_para_real(valor, dolar=3.30):
            return valor * dolar

Utilização da função:

.. doctest::

        >>> dolar_para_real(30)
        99.0

        >>> dolar_para_real(50, 3.40)
        170.0

        >>> dolar_para_real(valor=100, dolar=3.50)
        350.0

        >>> dolar_para_real(dolar=3.50, valor=200)
        700.0

        >>> dolar_para_real(valor=200)
        660.0

.. warning::

        Cuidado com listas como argumentos opcionais!

A criação da lista como argumento com valor padrão faz com que a mesma lista
mantenha-se para as múltiplas chamadas que normalmente não é o resultado
desejado.

.. testcode::

        def anexa_errado(elem, lista=[]):
            lista.append(elem)
            return lista

.. doctest::

        >>> x = anexa_errado(10)
        >>> x
        [10]

        >>> anexa_errado(5)
        [10, 5]

        >>> y = anexa_errado(20, x)
        >>> y
        [10, 5, 20]

A criação **correta** de listas deve ser realizada **dentro** da função e o
argumento com valor padrão deve recebe ``None`` para que seja possível
identificar quando a lista deve ser criada.

.. testcode::

        def anexa_correto(elem, lista=None):
            if not lista:
                lista = []
            lista.append(elem)
            return lista

.. doctest::

        >>> z = anexa_correto(10)
        >>> z
        [10]

        >>> anexa_correto(5)
        [5]

        >>> w = anexa_correto(20, z)
        >>> w
        [10, 20]
