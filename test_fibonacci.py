from unittest import TestCase

from fibonacci import fib


class TesteFibonacci(TestCase):
    """
    Utilizando a biblioteca ``unittest`` para verificar a funcionalidade do
    módulo com funções que geram a sequencia de Fibonacci
    """

    def test_fibonacci_invalid_argument(self):
        """
        Teste da entrada de argumentos inválidos na função que calcula a
        sequencia de Fibonacci
        """

        sequence = fib(-1)
        self.assertEqual(sequence, [])

    def test_fibonacci(self):
        """
        Teste da função que calcula a sequencia de Fibonacci utilizando uma
        entrada válida
        """

        sequence = fib(100)
        self.assertEqual(sequence, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
