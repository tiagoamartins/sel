.. _list:

Listas
======

Listas são estruturas de dados compostas. Elas são primeiramente utilizadas para
agrupar diversos valores.

Declaração
----------

Em Python essa estrutura se chama *list* e são formadas de elementos separados
por vírgulas ``,`` entre colchetes ``[]``.

Exemplo::

   [1, 2, 3]
   ['a', 'b', 'c']
   [True, False, True]

Além disso, listas podem armazenar diferentes tipos de valores diferentes::

   [1, 'a', True]

Também é possível armazenar outras listas::

   [1, 'a', True, [2, 'b', False]]

Utilização
----------

Pode-se atribuir um nome a uma lista criando assim uma variável:

.. doctest::

   >>> quadrados = [1, 4, 9, 16, 25]
   >>> quadrados
   [1, 4, 9, 16, 25]

Para obter um elemento de uma lista, assim como para ``strings``,
pode-se utilizar os índices dos elementos:

.. doctest::

   >>> quadrados[0]
   1
   >>> quadrados[-1]
   25

Fatiamento da lista também pode ser utilizado para obter uma sub lista:

.. doctest::

   >>> quadrados[2:4]
   [9, 16]
   >>> quadrados[-3:]
   [9, 16, 25]
   >>> quadrados[:4]
   [1, 4, 9, 16]

Cada operação de fatiamento retorna uma nova lista contendo os elementos
desejados. Isso significa que o exemplo abaixo retorna uma nova cópia da lista:

.. doctest::

   >>> quadrados[:]
   [1, 4, 9, 16, 25]

Iterações
---------

Comando ``for``
^^^^^^^^^^^^^^^

.. doctest::

   >>> numeros = [1, 2, 3, 4, 5, 6, 7]
   >>> quadrados = []
   >>> for numero in numeros:
   ...     quadrados.append(numero ** 2)
   >>> quadrados
   [1, 4, 9, 16, 25, 36, 49]

*List Comprehensions*
^^^^^^^^^^^^^^^^^^^^^

.. doctest::

   >>> quadrados_impares = [numero ** 2 for numero in numeros if numero % 2 == 1]
   >>> quadrados_impares
   [1, 9, 25, 49]
