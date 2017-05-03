"""
>>> numeros = [1, 2, 3, 4, 5, 6, 7]
>>> quadrados = []
>>> for numero in numeros:
...     quadrados.append(numero ** 2)
>>> quadrados
[1, 4, 9, 16, 25, 36, 49]

>>> quadrados_impares = [numero ** 2 for numero in numeros if numero % 2 == 1]
>>> quadrados_impares
[1, 9, 25, 49]
"""
