"""
>>> a, b = 10, 0

>>> try:
...     a / b
... except ZeroDivisionError:
...     print('Erro: tem que ver isso daí')
Erro: tem que ver isso daí

>>> b = "0"
>>> try:
...     a / b
... except (ZeroDivisionError, TypeError):
...     print('Erro: tem que ver isso daí')
Erro: tem que ver isso daí

>>> b = "0"
>>> try:
...     a / b
... except ZeroDivisionError:
...     print('Não é possível dividir por 0')
... except TypeError:
...     print('Algum tipo está errado')
Algum tipo está errado


>>> a = {}
>>> try:
...     print(a['chave'])
... except KeyError as exc:
...     print(type(exc))  # imprime o tipo da exceção
...     print(exc.args)  # mostra a tupla de argumentos que a exceção recebeu
...     print(exc)  # imprime diretamente os argumento
<class 'KeyError'>
('chave',)
'chave'
"""


class NetworkNotFoundError(Exception):
    pass


raise NetworkNotFoundError
